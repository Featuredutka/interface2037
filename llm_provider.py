from abc import ABC, abstractmethod
from typing import List

class LLMProvider(ABC):
    @abstractmethod
    def generate_response(self, prompt: str, model: str = "llama3") -> str:
        pass

    @abstractmethod
    def get_models(self) -> List[str]:
        pass
