from jsonschema import validate
from jsonschema import SchemaError

raw_prompt_schema = {
    "model_information": {
        "type": "string",
        "description": "Just the name of llm model currently use",
    },
    "origin_system_prompt": {
        "type": "string",
        "description": "just the user prompt as string here without the schema",
    },
    "origin_prompt": {
        "type": "string",
        "description": "just the user prompt as string here without any edit",
    },
    "refined_prompt": {
        "type": "string",
        "description": "Generate a refined version of user prompt",
    },
    "system_prompt_general": {
        "type": "string",
        "description": "Generate system prompt, must assign role and define general task related to assigned role",
    },
    "system_prompt_specific": {
        "type": "string",
        "description": "Generate system prompt, must assign role and define verify specific task related to assigned role",
    },
    "clairification_question": {
        "type": "array",
        "description": "list out questions to clarify the user prompt, must have atleast 1 question",
    },
    "rating": {"type": "integer", "description": "Rate user prompt from 1 to 10"},
    "tags": {
        "type": "array",
        "description": "list of possible metadata tags, must include 'prompting'",
    },
    "created_date": {
        "type": "string",
        "description": "This is date time generated completed, follwing format: YYYYY-MM-DD hh:mm",
    },
    "Author": {"type": "string", "description": "fix value 'hieutrungvu.ds.ai'"},
}

refined_prompt_schema = {
    "input_raw_prompt": {
        "type": "string",
        "description": "This is just user input prompt",
    },
    "input_system_prompt": {
        "type": "string",
        "description": "This is just what system prompt you are currently using (without the schema)",
    },
    "refined_output_prompt": {
        "type": "string",
        "description": "The most finetuned user prompt",
    },
    "refined_system_output_prompt": {
        "type": "string",
        "description": "The most finetuned System prompt for refined_output_prompt",
    },
    "clairification_question": {
        "type": "array",
        "description": "list out questions to clarify the prompt",
    },
    "rating": {"type": "integer", "description": "Rate the output prompt from 1 to 10"},
    "tags": {
        "type": "array",
        "description": "list of possible metadata tags, must include 'prompting'",
    },
    "created_date": {
        "type": "string",
        "description": "This is date time generated completed, follwing format: YYYYY-MM-DD hh:mm",
    },
    "Author": {"type": "string", "description": "fix value 'hieutrungvu.ds.ai'"},
}


def validate_schema(object, schema):
    try:
        validate(object, schema=schema)
    except SchemaError:
        print("Result failed validation, e: " + SchemaError)
    else:
        print("Passed validation")
