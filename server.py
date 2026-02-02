from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv("/opt/kaligpt/.env")

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

saldo = 50000

@app.post("/ask")
async def ask(data: dict):
    global saldo

    pergunta = data.get("pergunta")

    if saldo <= 0:
        return {"resposta": "Sem saldo suficiente."}

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": pergunta}],
        temperature=0.2
    )

    tokens = resp.usage.total_tokens
    saldo -= tokens

    return {
        "resposta": resp.choices[0].message.content,
        "tokens_usados": tokens,
        "saldo_restante": saldo
    }
