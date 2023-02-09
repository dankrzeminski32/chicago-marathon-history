FROM node:18.14.0-alpine
RUN mkdir /frontend
WORKDIR /frontend
COPY package.json /frontend/package.json
RUN npm install