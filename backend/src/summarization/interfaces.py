from abc import ABC, abstractmethod


class Summarization(ABC):
    @abstractmethod
    def summarize(self, text: str) -> str:
        """
        Método abstrato para sumarizar um dado texto.

        Args:
            text (str): O texto a ser sumarizado.

        Returns:
            str: O texto sumarizado.
        """
        pass
