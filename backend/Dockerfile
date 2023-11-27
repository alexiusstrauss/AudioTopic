FROM python:3.10.6-slim-buster

ENV APP_NAME=audiotopic-api
ARG DEV_MODE=true
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ America/Sao_Paulo
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update -yy  \
    && apt-get upgrade -yy \
    && apt-get install -yy libpq-dev git nano\
    && pip install --upgrade pip \
    && pip install --no-cache-dir pipenv

COPY Pipfile* .

RUN bash -c "if [ $DEV_MODE == 'true' ] ; \
    then pipenv install --dev ; else pipenv install; fi"

COPY . .

ENV PYTHONPATH $PROJECT_DIR/src:$PYTHONPATH

EXPOSE 8000

# Comando para rodar a aplicação
CMD ["pipenv", "run", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
