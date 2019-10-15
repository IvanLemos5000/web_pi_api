FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --update nodejs nodejs-npm 
RUN	npm install -g nodemon

COPY . .

CMD [ "nodemon", "./main.py" ]