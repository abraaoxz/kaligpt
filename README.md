# ⚔️ KaliGPT — ChatGPT no Terminal do Kali Linux

> Cliente CLI minimalista para usar a OpenAI direto do terminal.
> Criado por **[@abraaoxz](https://github.com/abraaoxz)** para quem vive no Kali, CTFs e pentesting.

---

## 🧠 O que é o KaliGPT?

O **KaliGPT** é um cliente de linha de comando que permite conversar com o ChatGPT **diretamente no terminal**, sem navegador, sem servidor web, sem interface gráfica.

Feito para quem:

* Vive no terminal
* Faz CTF
* Trabalha com pentesting
* Usa Kali Linux / Parrot OS diariamente
* Quer respostas rápidas sem sair do shell

---

## 🎯 Filosofia do projeto

> Simples. Direto. Funcional.

Sem:

* Painel web
* Banco de dados
* Sistema de usuários
* Complexidade desnecessária

Apenas você + terminal + OpenAI.

---

## ⚙️ Requisitos

* Kali Linux / Debian-based
* Python 3.10+
* Git
* Conta OpenAI com créditos ativos

---

## 🚀 Instalação em 1 comando

```bash
git clone https://github.com/abraaoxz/kaligpt.git
cd kaligpt
bash install.sh
```

O instalador faz tudo:

* Cria venv
* Instala dependências
* Solicita sua `OPENAI_API_KEY`
* Cria o comando global `kaligpt`

---

## 🔑 API Key

Durante a instalação, será solicitada sua chave.

Ou manualmente no arquivo:

```
.env
```

Formato:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

---

## ▶️ Como usar

Ative o ambiente (se necessário):

```bash
cd kaligpt
source venv/bin/activate
```

Execute:

```bash
kaligpt
```

Ou:

```bash
python kaligpt.py
```

Para sair:

```
sair
```

---

## 💬 Exemplos reais de uso

```
[kali-gpt]# melhores técnicas de enumeração em CTF
[kali-gpt]# explique esse erro do nmap
[kali-gpt]# como analisar um binário ELF
[kali-gpt]# como funciona privilege escalation no linux
```

---

## 📁 Estrutura do projeto

```
kaligpt/
 ├─ kaligpt.py
 ├─ install.sh
 ├─ requirements.txt
 ├─ .gitignore
 └─ README.md
```

---

## ❗ Erro comum: 429 insufficient_quota

Se aparecer:

```
429 insufficient_quota
```

Não é erro do projeto.

Significa que sua conta OpenAI está sem créditos:

[https://platform.openai.com/account/billing](https://platform.openai.com/account/billing)

---

## 🔐 Segurança

* `.env` está no `.gitignore`
* Sua API key nunca vai para o GitHub
* Tudo roda localmente

---

## 🛠️ Personalização

Você pode adaptar o KaliGPT facilmente para:

* Respostas focadas em pentesting
* Automatizar tarefas
* Integrar com scripts do seu laboratório

---

## 👤 Autor

Desenvolvido por **[@abraaoxz](https://github.com/abraaoxz)**
Focado em Kali Linux, CTFs e segurança ofensiva.

---

## ⭐ Contribua

Forks, melhorias e adaptações são bem-vindas.
Sinta-se livre para moldar ao seu workflow de pentest.
