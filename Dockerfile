FROM python:3.7

MAINTAINER Faiyaz Hasan "faiyaz.hasan1@gmail.com"

COPY . /app

WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN pytest

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
