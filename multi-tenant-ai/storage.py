import os

BASE_PATH = "data"

def load_documents(client: str) -> str:
    client_path = os.path.join(BASE_PATH, client)

    if not os.path.exists(client_path):
        return ""

    documents = []

    for filename in os.listdir(client_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(client_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    return "\n\n".join(documents)
