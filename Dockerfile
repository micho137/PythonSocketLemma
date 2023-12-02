FROM python:3.8-slim

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "-p", "4890"]