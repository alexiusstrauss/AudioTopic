# AudioTopic
  
![AudioTopic Template](AudioTopic-Template.png)

**AudioTopic**  é um projeto com base em um teste para processar arquivos de áudio nos formatos: .mp3 ou .wav
converter em texto usando a tecnologia STT, fazer um resumo deste conteúdo utilizando LLM e criar um áudio do resumo, disponibilizando para ouvir ou fazer download do resumo.
Segue o link para leitura do desfio técnico e suas especificações.
[Arquivo de especificações](AudioTipic-test.pdf)



### Backend
No backend utilizei a linguagem **python na versão 3.10** e o framework **FastAPI** na construção da api.
Utilizei o padrão de projeto "**Strategy**" para implementar através de uma interface a engine que será usada para resumir o texto usando LLM. Deixei disponível três engines: **LangChain**, **Tensorflow** e **LiteLLM**. Seguindo o **SOLID** e **Clean Code**, deixando código mais flexível e fácil de testar ou dar manutenção.
Para rodar os testes automatizados via Docker basta rodar o comando: `make test-api` caso o container esteja rodando, ou `docker exec -ti audiotopic-api pipenv run pytest`. 

Deverá configurar um .env na pasta backend/src/ com as credenciais da OPENAI para utilização do serviço com LangChain ou LiteLLM.
Ou configurar as credencias no docker-compose.yaml

    OPEN_AI_TOKEN=sk-change-me
    TENSORFLOW_MODEL_NAME="t5-small"

No arquivo **api.py** poderá configurar qual engine usar para o processo de resumo escolhendo LangChain, TensorFlow ou LiteLLM:

  
    service = DeepDive(llm_engine=LLM_ENGINES.get("LangChain"))
    service = DeepDive(llm_engine=LLM_ENGINES.get("TensorFlow"))
    service = DeepDive(llm_engine=LLM_ENGINES.get("LiteLLM"))

**Tecnologias utilizadas:**
 - Python 3.10 
 - Pipenv
 - FastAPI
 - Pytest e Pytest-cov
 - Docker
 - Make


### Frontend
Utilizei o framework Nuxt3 e criei um componente responsável consumir a API.
**Tecnologias utilizadas:**
 - Nuxt3 
 - Javascript
 - Docker
 - Make  

 
Ao rodar o comando: `make up` na raiz do projeto, será criado as imagens docker do audiotopic-api e audiotopic-app
e iniciado os serviços via docker-compose up.
o serviço: audiotopic-app vai aguardar que o serviço: audiotopic-api fique online e disponível para ficar online.
se tudo estiver ok você poderá acessar o swagger da api no endereço: http://127.0.0.1:8000/docs
e poderá acessar o app na página: http://127.0.0.1:3000.

### Arquivo para teste:
na pasta 'audios' contem dois arquivos para testar a aplicação.