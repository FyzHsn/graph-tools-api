FROM python:3.7

MAINTAINER Faiyaz Hasan "faiyaz.hasan1@gmail.com"

COPY . /app

WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
