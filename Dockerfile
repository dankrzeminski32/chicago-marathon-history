FROM python:3.9

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser


WORKDIR /home/Chicago_Marathon_History

ADD ./src/scrapers/history.py .

COPY requirements.txt /tmp/requirements.txt


RUN python3 -m pip install -r /tmp/requirements.txt

CMD python history.py