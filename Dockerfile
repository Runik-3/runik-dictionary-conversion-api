FROM ubuntu

EXPOSE 8000:8000

RUN apt update -y && apt upgrade -y
RUN apt install -y zip
RUN apt install -y python3 
RUN apt install -y python3-pip
RUN pip3 install pipenv
RUN pip3 install pyglossary

WORKDIR /runik
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock

RUN pipenv install --deploy --system

COPY app ./app
COPY server.py ./server.py
COPY dictionaries ./dictionaries

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "server:app", "-t", "160"]