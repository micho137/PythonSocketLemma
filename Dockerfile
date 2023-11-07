FROM python:3.8.3-alpine3.11

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y build-essential libatlas-base-dev

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "/src/app.py"]