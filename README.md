# Open Source Chatbot

A lightweight, open-source chatbot starter built with FastAPI and a local Ollama model.

## Features
- Local LLM support via Ollama
- Simple REST API
- Web UI in the browser
- Easy to extend

## Requirements
- Python 3.10+
- Ollama installed locally
- A model pulled into Ollama, for example:
  - `ollama pull llama3.2`

## Quick Start

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

4. Start Ollama:
   ```bash
   ollama serve
   ```

5. Pull a model:
   ```bash
   ollama pull llama3.2
   ```

6. Run the chatbot app:
   ```bash
   python app.py
   ```

7. Open the browser:
   - http://localhost:8000

## API
### Health check
```bash
curl http://localhost:8000/api/health
```

### Chat
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello there!","history":[]}'
```

## Notes
This project is intentionally simple and open-source-friendly. You can replace Ollama with another model provider or add:
- authentication
- persistent chat storage
- user accounts
- a proper database
- Docker deployment
- streaming responses

## License
MIT
