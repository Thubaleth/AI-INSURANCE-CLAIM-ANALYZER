import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def create_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

chunks = [
    {
        "filename": "car_claims.txt",
        "content": "Customers should provide photographs showing the damage to the vehicle."
    },
    {
        "filename": "car_claims.txt",
        "content": "A police report may be required for a car accident claim."
    },
    {
        "filename": "home_claims.txt",
        "content": "Customers should provide photographs of property damage."
    }
]


for chunk in chunks:

    chunk["embedding"] = create_embedding(chunk["content"])


for chunk in chunks:

    print("Filename:", chunk["filename"])
    print("Content:", chunk["content"])
    print("Embedding length:", len(chunk["embedding"]))
    print("First 5 numbers:", chunk["embedding"][:5])
    print("-----------------------------")