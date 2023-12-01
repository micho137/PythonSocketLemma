#FROM python:3.8
#WORKDIR /app
#COPY . .
#RUN pip install -r requirements.txt
#CMD ["python3", "./src/app.py"]

FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
COPY src/ src/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4890
CMD ["gunicorn", "-k", "eventlet", "main:app"]
