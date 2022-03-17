FROM python:3-alpine3.6

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py" ]

