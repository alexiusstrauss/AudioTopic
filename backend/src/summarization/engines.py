from http import HTTPStatus

import requests
from langchain.llms.openai import OpenAI
from src.services.exceptions import ApiKeyException
from src.summarization.interfaces import Summarization
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM


class LiteLLMFlow(Summarization):
    def __init__(self, url_api: str, api_key: str, model: str):
        self.url_api = url_api
        self.api_key = api_key
        self.model = model

    def summarize(self, text: str) -> str:
        """
        Envia o texto para a API do LiteLLM e recebe um resumo
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "Você é um assistente especializado em criar resumos concisos e informativos."},
                {"role": "user", "content": f"Analise o texto e crie um resumo breve com as informações mais relevantes. O resumo deve ser conciso, destacando apenas os aspectos mais importantes do texto.\n\nTexto para análise: {text}"}
            ],
            "temperature": 0.3,
            "max_tokens": 500
        }
        
        try:
            response = requests.post(
                f"{self.url_api}/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Extrair a resposta do modelo
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"].strip()
            else:
                raise ValueError("Resposta inesperada da API LiteLLM")
                
        except Exception as exc:
            print(f"Erro ao chamar a API LiteLLM: {exc}")
            raise ApiKeyException() from exc
            
    def token_is_valid(self):
        """
        Verifica se o token da API é válido
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": "Olá"}
            ],
            "max_tokens": 5
        }
        
        try:
            response = requests.post(
                f"{self.url_api}/chat/completions",
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code in [
                HTTPStatus.UNAUTHORIZED,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.FORBIDDEN,
            ]:
                raise ApiKeyException()
                
        except Exception as exc:
            raise ApiKeyException() from exc


class LangChain(Summarization):
    def __init__(self, api_key: str):
        self.llm = OpenAI(temperature=0, api_key=api_key, model="gpt-3.5-turbo-instruct")
        self.api_key = api_key

    def summarize(self, text: str) -> str:
        prompt = f"analise o texto e crie um resumo breve, \
                  com as informações mais relevantes. \
                  O resumo deve ser conciso \
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
                timeout=15,
            )
        except Exception as exc:
            raise ApiKeyException() from exc

        if response.status_code in [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.FORBIDDEN,
        ]:
            raise ApiKeyException()


class TensorFlow(Summarization):
    pass
    # def __init__(self, model_name="t5-small"):
    #     self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    #     self.model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

    # def summarize(self, text: str, max_length=650):
    #     # Preparar a entrada para o modelo
    #     inputs = self.tokenizer.encode(f"summarize: {text}", return_tensors="tf", max_length=1600, truncation=True)
    #     # Gerar a saída do modelo
    #     summary_ids = self.model.generate(
    #         inputs,
    #         max_length=max_length,
    #         length_penalty=4.0,
    #         num_beams=4,
    #         early_stopping=True,
    #     )
    #     return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
