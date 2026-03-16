from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

generator = pipeline(
    "text-generation",
    model="../models"
)

@app.get("/ask")
def ask(question: str):

    prompt = f"""
You are a domain expert assistant.

Question:
{question}

Answer:
"""

    result = generator(prompt, max_length=200)

    return {"response": result[0]["generated_text"]}
