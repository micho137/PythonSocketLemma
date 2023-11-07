FROM python:3.8.3-alpine3.11

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip install atlas

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "/src/app.py"]