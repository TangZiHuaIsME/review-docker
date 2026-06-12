FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
RUN chmod +x wait-for-it.sh
EXPOSE 3000
CMD ["./wait-for-it.sh","db:5432","--","npm","start"]
