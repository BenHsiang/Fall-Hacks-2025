# CALCFOOD

Project: Food ordering app but in order to use it, you must solve various math equations.

This project runs a local AI model with Ollama to generate and check simple Calculus I math questions.
It uses:

Ollama (for running the model locally)

FastAPI (backend server)

HTML + JavaScript (frontend with KaTeX to render math)

1. Install Ollama

Download Ollama here:  htps://ollama.com/download

Then pull the model:

```bash
# Pull the Ollama model
ollama pull qwen2.5:7b-instruct

# Run the FastAPI server
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```
