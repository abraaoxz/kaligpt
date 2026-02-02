from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
import requests

console = Console()
history = FileHistory("/opt/kaligpt/.history")

API_URL = "http://127.0.0.1:8000/ask"

def ask_server(question):
    r = requests.post(
        API_URL,
        json={"pergunta": question},
        timeout=60
    )
    data = r.json()
    return f"""{data.get('resposta')}

[TOKENS]: {data.get('tokens_usados')} | [SALDO]: {data.get('saldo_restante')}
"""

console.print("[bold green]KaliGPT Local Client[/bold green]")

while True:
    user = prompt("[kali-gpt]# ", history=history)
    if user.lower() == "exit":
        break

    console.print("[cyan]Pensando...[/cyan]")
    resposta = ask_server(user)
    console.print(resposta)
