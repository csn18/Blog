FROM node:14.9

WORKDIR /app/front

COPY package*.json .
COPY entrypoint.sh .

RUN npm install
RUN chmod +x ./entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/app/front/entrypoint.sh"]