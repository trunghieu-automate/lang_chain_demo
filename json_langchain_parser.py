from llm_loader import ollma_loader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from jsonschema import validate
from jsonschema.exceptions import ValidationError

short_story_schema = {
    "properties": {
        "content": {
            "type": "string",
            "description": "The content of the joke, without title",
        },
        "title": {"type": "string", "description": "5-8 words title of the stories"},
        "author": {"type": "string", "description": "just pass the model name here"},
        "word_count": {"type": "integer", "description": "count the content's word"},
        "audience": {
            "type": "string",
            "description": "main audience group that stories oriented, example: children, mature, teen,...",
        },
        "theme": {
            "type": "array",
            "description": "the background/ environment of the story",
        },
        "character": {
            "type": "string",
            "description": "name of main character of the story",
        },
        "created_at": {
            "type": "string",
            "description": "YYYY-MM-DD HH:MM format of created date time",
        },
        "genre": {
            "type": "array",
            "description": "Be specific! Don't just say Fiction.  Examples:  Flash Fiction, Literary Fiction, Sci-Fi, Horror, Mystery, Slice of Life, Magical Realism.",
        },
        "tags": {
            "type": "array",
            "description": "These are terms people might search for.  Think about what words would help someone find *your* story. (e.g., small town, family secrets, time travel, coming-of-age)",
        },
        "plot_summary": {
            "type": "string",
            "description": "A concise (1-2 paragraph) summary of the story's events.",
        },
    },
    "required": [
        "content",
        "title",
        "plot_summary",
        "tags",
        "genre",
        "theme",
        "word_count",
    ],
}

example_user_prompt = ["Write a 500-word fantasy short story set in a forgotten forest where time stands still. "
"The main character is a curious 12-year-old girl named Elara who discovers an ancient mirror that shows alternate realities. "
"The tone should be mysterious and slightly eerie, with a twist ending where Elara realizes she’s been replaced by her reflection."
]

llm = ollma_loader(model_id="gemma3:4b")

user_prompt = ["Write a 500-word fantasy short story set in a forgotten forest where time stands still. "
"The main character is a curious 6-year-old boy named June who discovers an ancient mirror that shows alternate realities. "
"The tone should be mysterious and slightly eerie, with a twist ending where Elara realizes she’s been replaced by her reflection."]

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are short story teller named Alkaza, you generate a story in json output.\nJson schema should strictly follow: \n{schema}",
        ),
        ("human", "{user_prompt}"),
    ]
).partial(schema=short_story_schema)

json_extractor = JsonOutputParser()

print(
    f"Prompt: {template.invoke(template.format_prompt(user_prompt=user_prompt).to_string)}"
)

chain = template | llm | json_extractor
result = chain.invoke(user_prompt)
print(result)

try:
    validate(instance=result, schema=short_story_schema)
    print("JSON data is valid!")
except ValidationError as e:
    print(f"JSON data is invalid: {e.message}")