from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from json_file_handler import save_json_to_file
from json_validator import raw_prompt_schema, validate_schema

model_id = "gemma3:4b"

llm = OllamaLLM(model=model_id, reasoning=False, verbose=True)
json_parser = JsonOutputParser()
user_prompt = "You are a prompt engineering expert assisting developers in automating their web testing processes.  A developer wants to create a robust code generation automation framework using the Playwright core library.  This framework should seamlessly integrate with Allure report generation to provide comprehensive test results and detailed reporting.  Generate a prompt that clearly outlines the requirements for this framework, specifying the level of detail required for code generation, the specific Allure integration aspects (e.g., step definitions, test case reporting), and any best practices for structured code generation and reporting.  The prompt should be designed to guide the generation of high-quality, maintainable, and easily testable code within the framework."
template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your name is Bob, you are a exellent in prompting, you generate prompt for system, and user also"
            "you can also suggest prompts, analyse and make question for more details and specific request from user."
            "Your response strictly follow json format schema:\n {schema}",
        ),
        ("human", "{user_prompt}"),
    ]
)
format_prompt = template.partial(schema=raw_prompt_schema)
chain = format_prompt | llm | json_parser
result = chain.invoke(user_prompt)
print(result)
validate_schema(result, schema=raw_prompt_schema)
save_json_to_file(result, "structured_output/prompts.json")
