FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY app/requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .
COPY models /app/models

EXPOSE 8000
CMD [ "python", "app/main.py" ]
