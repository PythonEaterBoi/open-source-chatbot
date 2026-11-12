import httpx
from typing import List, Dict, Optional
from config import MODEL_NAME, OLLAMA_BASE_URL, SYSTEM_PROMPT


class Chatbot:
    def __init__(self, model_name: str = MODEL_NAME, base_url: str = OLLAMA_BASE_URL):
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")

    def build_prompt(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        conversation = [f"System: {SYSTEM_PROMPT}"]

        if history:
            for turn in history:
                role = turn.get("role", "user")
                content = turn.get("content", "")
                if role == "assistant":
                    conversation.append(f"Assistant: {content}")
                else:
                    conversation.append(f"User: {content}")

        conversation.append(f"User: {message}")
        conversation.append("Assistant:")
        return "\n".join(conversation)

    async def generate(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        prompt = self.build_prompt(message, history)

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(f"{self.base_url}/api/generate", json=payload)
                response.raise_for_status()
                data = response.json()
                reply = data.get("response", "").strip()
                return reply if reply else "I’m here, but I didn’t get a useful response from the model."
        except Exception as exc:
            return (
                "I couldn’t reach the local model server. "
                "Please make sure Ollama is installed and running, and that the model is pulled. "
                f"Error: {exc}"
            )
