import os

from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OLLAMA_API_KEY"))


if __name__ == "__main__":
    main()
