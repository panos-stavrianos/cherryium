FROM node:8.7.0-alpine
RUN apk add --no-cache git
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./package.json /usr/src/app/
RUN npm install && npm cache clean --force
COPY ./ /usr/src/app
RUN npm run build
FROM python:3.7
# here build/do what you want to do
WORKDIR /usr/src/app
RUN ls -a
COPY ./requirements.txt /usr/src/app/
RUN ls -a
RUN pip3 install -r requirements.txt
COPY ./ /usr/src/app
COPY --from=0 /usr/src/app/app/static ./app/static
RUN ls -a
EXPOSE 80
CMD gunicorn -b 0.0.0.0:80 --worker-class=gevent -w 4 app:app