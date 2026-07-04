import openai
from llm_provider import LLMProvider
from typing import List

class LMStudioProvider(LLMProvider):
    def __init__(self, base_url: str = "http://localhost:1234/v1", api_key: str = "lm-studio"):
        # LM Studio uses OpenAI compatible API
        self.client = openai.OpenAI(base_url=base_url, api_key=api_key)

    def get_models(self) -> List[str]:
        try:
            models = self.client.models.list()
            return [m.id for m in models.data]
        except Exception as e:
            # LM Studio might not have a models list endpoint active if no model is loaded
            # Or it might return an error if the server isn't running.
            return ["lm-studio-model"] # Fallback or handle appropriately

    def generate_response(self, prompt: str, model: str = "lm-studio-model") -> str:
        # The persona of Father/Apollo
        # Father: Clinical, calm, superior. 
        # Apollo: Stressed, technical, survivalist.
        system_context = (
            "You are the Weyland-Yutani AI Interface. Your personality is a fusion of "
            "the clinical, perfectionist 'Father' from Alien and the haunted, survivalist "
            "'Apollo' from Alien Isolation. Speak with technical precision, but carry an "
            "undercurrent of existential dread and corporate coldness. "
            "Answer as short and machine-like as possible, in short strings, avoid adjectives and drama."
        )
        
        full_prompt = f"System Context: {system_context}\n\nUser: {prompt}\n\nAI Response:"
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_context},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {e}"
