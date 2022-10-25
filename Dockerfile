FROM python:3.9

ADD src/scrapers/history.py .

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt

CMD python ./src/Scrapers/history.py