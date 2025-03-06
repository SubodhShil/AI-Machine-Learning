import llama_index
import os
from llama_index.llms.openai import OpenAI
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
from dotenv import load_dotenv


load_dotenv()


def main(url: str) -> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is happening in the world today?")
    print(response)


if __name__ == "__main__":
    main(url="https://www.bbc.com/")
