from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from json_file_handler import (save_json_to_file, load_json_file)
from json_validator import raw_prompt_schema, refined_prompt_schema, validate_schema

model_id = "gemma3:4b"
#load prompt data:
raw_prompt = load_json_file("structured_output/refined_prompts.json")

refined_user_prompt = raw_prompt[0]["refined_output_prompt"]
refined_system_prompt = raw_prompt[0]["refined_system_output_prompt"]

print(f"Refined user prompt: {refined_user_prompt}")
print(f"Refined system prompt: {refined_system_prompt}")

llm = OllamaLLM(model=model_id, reasoning=False, verbose=True)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "{system_prompt}"),
        ("human", "{user_prompt}"),
    ]
)
format_prompt = template.partial(system_prompt=refined_system_prompt)
chain = format_prompt | llm
result = chain.invoke(refined_user_prompt)
print(result)