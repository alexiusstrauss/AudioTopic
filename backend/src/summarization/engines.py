from http import HTTPStatus

import requests
from langchain.llms.openai import OpenAI
from src.services.exceptions import ApiKeyException
from src.summarization.interfaces import Summarization


class LangChain(Summarization):
    def __init__(self, api_key: str):
        self.llm = OpenAI(temperature=0, api_key=api_key)
        self.api_key = api_key

    def summarize(self, text: str) -> str:
        prompt = f"Por favor, analise o seguinte texto e crie um resumo muito breve, \
                  apenas com as informações mais relevantes. \
                  O resumo deve ser conciso, com poucas palavras, \
                  destacando apenas os aspectos mais importantes do texto. \
                  Aqui está o texto para análise: \n\n{text}\n\n Sumário:"
        return self.llm.predict(prompt)

    def token_is_valid(self):
        url = "https://api.openai.com/v1/engines/davinci-codex/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "prompt": "Translate the following English text to French: 'Hello, world!'",
            "max_tokens": 10,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=10,
            )
        except Exception as exc:
            raise ApiKeyException() from exc

        if response.status_code in [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.FORBIDDEN,
        ]:
            raise ApiKeyException()


class TensorFlowStrategy(Summarization):
    def __init__(self):
        pass

    def summarize(self, text: str) -> str:
        return "Texto sumarizado com TensorFlow"
