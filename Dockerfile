FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4890
CMD ["gunicorn", "--bind", "0.0.0.0:4890", "app:app"]
