FROM python:3.10

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY models/ ./models/
COPY app/templates /app/templates

EXPOSE 8000
CMD ["python", "app/main.py"]
