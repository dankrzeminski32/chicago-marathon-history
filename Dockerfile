FROM python:3.9

WORKDIR /home/Chicago_Marathon_History

ADD ./src/scrapers/history.py .

ADD requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

CMD python history.py