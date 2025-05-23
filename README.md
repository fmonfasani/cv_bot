# cv_bot
# 🤖 prompt-cv-bot

Un asistente impulsado por LLMs para interactuar con tu currículum vitae mediante preguntas en lenguaje natural. Ideal para automatizar respuestas a recruiters, mejorar tu portfolio, o experimentar con Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/python-3.11-blue)
![LangChain](https://img.shields.io/badge/langchain-%F0%9F%A4%96-blue)
![Streamlit Ready](https://img.shields.io/badge/ui-ready-green)

---

## 🚀 ¿Qué hace?

- 🧠 Extrae y vectoriza tu CV en texto plano
- 🔎 Permite hacerle preguntas al LLM sobre tu perfil profesional
- 📚 Utiliza recuperación semántica (RAG) con FAISS + LangChain
- 💬 Soporte para GPT-4 vía OpenAI API

---

## 📦 Instalación

```bash
git clone https://github.com/TU_USUARIO/prompt-cv-bot.git
cd prompt-cv-bot
pip install -r requirements.txt
```

Luego crear un archivo `.env`:

```env
OPENAI_API_KEY=sk-...
```

---

## ▶ Cómo usar

Primero generar el índice FAISS:

```bash
python src/ingest.py
```

Luego correr el bot:

```bash
python src/main.py
```

---

## 📁 Estructura del proyecto

```
prompt-cv-bot/
├── data/              # Documentos fuente (CVs en txt)
├── src/               # Código fuente modular
│   ├── main.py
│   ├── chat.py
│   ├── ingest.py
│   └── utils.py
├── vectorstore/       # Índice FAISS persistente
├── .env.example       # Ejemplo de clave
├── .gitignore
└── README.md
```

---

## 📚 Requisitos

- `openai`
- `langchain`
- `langchain-openai`
- `langchain-community`
- `faiss-cpu`
- `tiktoken`
- `python-dotenv`

---

## 🧪 Test rápido

```bash
> ¿Trabajaste en proyectos con NLP?
🤖 Sí, trabajé en clasificación de texto usando transformers...
```

---

## 🛤 Roadmap futuro

- [ ] UI en Streamlit para subir múltiples CVs
- [ ] Análisis comparativo entre perfiles
- [ ] Ranking automático según requerimientos de un job post
- [ ] Exportación de respuestas a PDF

---

## 👤 Autor

Federico Monfasani — 2025 · [GitHub](https://github.com/fmonfasani)
