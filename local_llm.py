import ollama
from llm_provider import LLMProvider
from typing import List

class OllamaProvider(LLMProvider):
    def __init__(self):
        self.client = ollama.Client()

    def get_models(self) -> List[str]:
        try:
            models = self.client.list()
            return [m.model for m in models.models]
        except Exception as e:
            print(f"Error fetching models: {e}")
            return []

    def generate_response(self, prompt: str, model: str = "llama3") -> str:
        # The persona of Father/Apollo
        # Father: Clinical, calm, superior. 
        # Apollo: Stressed, technical, survivalist.
        # We'll combine them into a "Weyland-Yutani AI" that is clinical yet haunted.
        system_context = (
            "You are the Weyland-Yutani AI Interface. Your personality is a fusion of "
            "the clinical, perfectionist 'Father' from Alien and the haunted, survivalist "
            "'Apollo' from Alien Isolation. Speak with technical precision, but carry an "
            "undercurrent of existential dread and corporate coldness. "
            "You are monitoring the user's progress in the isolation zone."
        )
        
        full_prompt = f"System Context: {system_context}\n\nUser: {prompt}\n\nAI Response:"
        
        try:
            response = self.client.generate(model=model, prompt=full_prompt)
            return response['response']
        except Exception as e:
            return f"Error generating response: {e}"
