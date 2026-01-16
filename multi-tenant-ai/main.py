from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import get_client
from storage import load_documents
from agent import AIAgent
import google.generativeai as genai
import os

# Configuration IA
genai.configure(
    api_key="AIzaSyALGkNRWYmAU3bv2mCBk5xc9rPXQg12Uto"
)
model = genai.GenerativeModel("gemini-2.5-flash")
agent = AIAgent(model)

app = FastAPI(title="Multi-tenant AI API")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query, client=Depends(get_client)):
    documents = load_documents(client)

    answer = agent.run(
        question=query.question,
        documents=documents
    )

    return {
        "client": client,
        "answer": answer
    }
