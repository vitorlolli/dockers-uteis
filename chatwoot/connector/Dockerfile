FROM node:16

RUN git clone https://github.com/unkbot/chatwoot-codechat

WORKDIR /chatwoot-codechat

RUN npm install

RUN npm run build

CMD npm run start

EXPOSE 1234