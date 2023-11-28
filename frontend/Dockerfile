FROM node:20

WORKDIR /app
RUN apt-get update && apt-get install -y netcat-openbsd

COPY ./src/package*.json ./

RUN npm install -g pnpm
RUN pnpm install

COPY ./src/ .

EXPOSE 3000

RUN chmod +x wait-for-api.sh

# Comando para iniciar o projeto
CMD ["pnpm", "run", "dev"]
