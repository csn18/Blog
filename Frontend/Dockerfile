FROM node:14.9

WORKDIR /app/Frontend

COPY package*.json .
COPY entrypoint.sh .

RUN npm install

COPY . .

ENTRYPOINT ["sh", "/app/Frontend/entrypoint.sh"]
