import os

def load_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path,filename)

        with open(file_path,"r") as file:
            content =file.read()

        documents.append({
            "filename": filename,
            "content": content
        })

    return documents



def chunk_text(text,chunk_size=200):

    chunks = []

    for i in range(0,len(text),chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks

documents = load_documents("documents")

for document in documents:
    chunks = chunk_text(document["content"])



print("\n==============================")
print(document["filename"])
print("==============================")

for chunk in chunks:
        print("\n--- CHUNK ---")
        print(chunk)


