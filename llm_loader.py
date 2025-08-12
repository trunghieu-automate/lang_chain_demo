from langchain_ollama import OllamaLLM

def ollma_loader(model_id='llama3.2:3b'):
    return OllamaLLM(
        model=model_id
    )