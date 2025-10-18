FROM python:3.10

RUN mdkir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY app /app
COPY models /app/models

EXPOSE 8000
CMD [ "python", "main.py" ]
