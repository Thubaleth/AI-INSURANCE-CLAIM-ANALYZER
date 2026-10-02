import os

def load_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        with open(file_path,"r") as file:
            content = file.read()

        documents.append({
            "filename" : filename,
            "content" : content
        })

    return documents

        
documents = load_documents("documents")

for document in documents:
    print(document["filename"])
        

        