FROM python:3-alpine3.6

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

COPY syntax.py /usr/local/lib/python3.6/site-packages/contracts/

CMD ["python", "app.py" ]

