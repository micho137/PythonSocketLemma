FROM python:3.8.3-alpine3.11

WORKDIR /python-docker

RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

COPY . .

CMD [ "python", "/src/app.py"]