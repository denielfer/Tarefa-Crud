FROM python:3.10-alpine as requirements-stage

RUN apk --update add gcc build-base libffi-dev
RUN pip install --upgrade pip

FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN apk --update add gcc build-base libffi-dev 

COPY . /usr/src/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD [ "uvicorn", "Tarefas.main:app", "--host", "0.0.0.0", "--port", "8000" ]