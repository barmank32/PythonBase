FROM python:3.8-buster

COPY ./requirements.txt ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN pip install -U pip && \
    pip install setuptools wheel && \
    pip install -r requirements.txt

WORKDIR /app
COPY ./app /app

ENTRYPOINT ["/entrypoint.sh"]
