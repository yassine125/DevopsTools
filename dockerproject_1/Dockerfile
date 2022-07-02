FROM node:16
LABEL MAINTAINER="abbassi.yassine@hotmail.fr"
ENV PORT=8080 \
	URL="www.google.com" \
	DB_CONNECTION="db-test"
USER 1000
WORKDIR /app/src
COPY . . 
#ADD 
RUN npm i express@4.16.1
RUN npm install
EXPOSE ${PORT}
CMD ["node","express.js"]