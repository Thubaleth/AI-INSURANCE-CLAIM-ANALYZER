import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=Api_key)


def create_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

embedding = create_embedding(
    "My car was involved in an accident."
)


print("Embedding length:", len(embedding))
print("First 10 numbers:", embedding[:10])