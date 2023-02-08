FROM python:3.10.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY  wsgi.py .env requirements.txt config.py /usr/src/app/
RUN pip install -r requirements.txt
COPY src/backend/ /usr/src/app/src/backend/

RUN ls -la /usr/src/app/*

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]