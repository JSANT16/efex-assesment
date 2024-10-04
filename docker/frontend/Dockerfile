FROM node:18-alpine

ENV VITEDIR=/frontend

RUN mkdir $VITEDIR

WORKDIR $VITEDIR

RUN npm install -g pnpm


COPY frontend/package.json frontend/pnpm-lock.yaml ./

RUN pnpm install

COPY frontend /$VITEDIR

