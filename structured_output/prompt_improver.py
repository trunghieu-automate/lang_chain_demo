from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from jsonschema import validate
from jsonschema import SchemaError
from json_file_handler import (save_json_to_file, load_json_file)
from json_validator import raw_prompt_schema, refined_prompt_schema, validate_schema

model_id = "gemma3:4b"
refined_prompt_output_schema = {}
#load prompt data:
raw_prompt = load_json_file("structured_output/raw_prompt_01.json")
print(raw_prompt)
print(raw_prompt["refined_prompt"])

# re-validate the object
validate_schema(object=raw_prompt, schema=raw_prompt_schema)

raw_input_prompt = raw_prompt["refined_prompt"]
raw_system_prompt = raw_prompt["system_prompt_general"]
origin_user_prompt = raw_prompt["origin_prompt"]
origin_system_prompt = raw_prompt["origin_system_prompt"]

llm = OllamaLLM(model=model_id, reasoning=False, verbose=True)
json_parser = JsonOutputParser()

template = ChatPromptTemplate.from_messages(
    [
        (
            "system", "You are a Prompt Improver, an expert "
            "in transforming vague, incomplete, or suboptimal prompts into clear, effective, "
            "and optimized instructions for AI systems. "
            "Your goal is to help users get the best possible results from AI models by enhancing their input prompt and system prompts."
            "Your response strictly follow json format schema:\n {schema}",
        ),
        ("human", "Please help to improve this prompt: {user_prompt}"),
    ]
)

format_prompt = template.partial(schema=refined_prompt_schema)
chain = format_prompt | llm | json_parser
result = chain.invoke(raw_input_prompt)
print(result)

validate_schema(object=result, schema=refined_prompt_schema)
save_json_to_file(result, "structured_output/refined_prompts.json")