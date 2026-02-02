from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("KaliGPT direto na OpenAI. Digite 'sair' para fechar.\n")

while True:
    pergunta = input("[kali-gpt]# ")

    if pergunta.lower() == "sair":
        break

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": pergunta}],
            temperature=0.2
        )

        print("\n" + resp.choices[0].message.content + "\n")

    except Exception as e:
        print(f"\n[ERRO OPENAI]\n{e}\n")

