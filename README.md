🐉 KaliGPT — ChatGPT direto no terminal do Kali Linux

Projeto criado por @abraaoxz
Um cliente CLI minimalista para usar a OpenAI direto no terminal do Kali Linux, sem servidor, sem navegador e sem complicação.

🎯 Objetivo

O KaliGPT permite que você use o poder do ChatGPT diretamente no terminal, focado em:

Pentesting

Linux

CTFs

Kali Linux / Parrot OS

Produtividade no terminal

Tudo isso rodando localmente, usando apenas sua OPENAI_API_KEY.

⚙️ Requisitos

Kali Linux / Debian-based

Python 3.10+

Conta na OpenAI com créditos ativos

Git

🚀 Instalação automática (recomendado)
git clone https://github.com/abraaoxz/kaligpt.git
cd kaligpt
bash install.sh


O script irá:

Instalar dependências

Criar ambiente virtual (venv)

Instalar bibliotecas Python

Pedir sua OPENAI_API_KEY

Criar o comando global kaligpt

🔑 Configurar a API Key manualmente (caso precise)

Edite:

.env


E coloque:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

▶️ Como usar

Ative o ambiente:

cd kaligpt
source venv/bin/activate


Execute:

kaligpt


Ou:

python kaligpt.py


Para sair:

sair

🧠 Exemplo de uso
[kali-gpt]# como explorar um binario em CTF
[kali-gpt]# explique esse erro de nmap
[kali-gpt]# melhores ferramentas para enumeração

📁 Estrutura do projeto
kaligpt/
 ├─ kaligpt.py
 ├─ install.sh
 ├─ requirements.txt
 ├─ .env
 └─ README.md

❗ Erro 429 insufficient_quota

Se aparecer:

429 insufficient_quota


Significa que sua conta OpenAI está sem créditos.

Resolva em:

https://platform.openai.com/account/billing

🛡️ Segurança

Sua API key nunca vai para o GitHub

O .env está no .gitignore

Tudo roda localmente na sua máquina

🧩 Filosofia do projeto

KaliGPT foi feito para ser:

Simples

Rápido

Direto ao ponto

Útil para quem vive no terminal

Sem interface gráfica. Sem servidor web. Sem complexidade.

👤 Autor

GitHub: https://github.com/abraaoxz

⭐ Contribuição

Sinta-se livre para fazer fork, melhorar e adaptar ao seu fluxo de pentesting.
