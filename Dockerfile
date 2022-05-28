
FROM python:3.8.11


WORKDIR /usr/app

RUN pip install --upgrade pip

COPY requirements.txt ./


RUN pip install -r requirements.txt


COPY . .

CMD [ "python3", "server.py" ]