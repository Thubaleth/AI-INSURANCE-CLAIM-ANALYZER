import numpy as np
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def cosine_similarity(vector1,vector2):
    vector1 =np.array(vector1)
    vector2 =np.array(vector2)

    similarity = np.dot(vector1,vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )

    return similarity


vector1 = [1,0,0]
vector2 = [1,0,0]

score = cosine_similarity(vector1,vector2)

print(score)

chunks = [
    {
        "filename": "car_claims.txt",
        "content": "Customers should provide photographs...",
        "embedding": [...]
    },
    {
        "filename": "car_claims.txt",
        "content": "A police report may be required...",
        "embedding": [...]
    }
]

def create_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


for chunk in chunks:
    chunk["embedding"] = create_embedding(chunk["content"])

query = "What documents do I need after a car accident?"
query_embedding = create_embedding(query)

best_chunk = None
best_score = -1

for chunk in chunks:

    score = cosine_similarity(
        query_embedding,
        chunk["embedding"]
    )

    if score > best_score:
        best_score = score
        best_chunk = chunk


print("Best match:")
print(best_chunk["content"])
print("Similarity:", best_score)