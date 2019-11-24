FROM python:3.8-alpine3.10
LABEL author="Chahkiev Magomed;OlegSchwann"

COPY . '/home/aidvantage'

RUN /usr/local/bin/python3.8 -m pip install --requirement /home/aidvantage/requirements.txt && \
    /usr/local/bin/python3.8 /home/aidvantage/manage.py migrate;

EXPOSE 8000
CMD ["/usr/local/bin/python3.8", "/home/aidvantage/manage.py", "runserver", "0.0.0.0:8000"]
# firefox "http://$( docker inspect $( docker ps --quiet ) --format='{{ .NetworkSettings.Networks.bridge.IPAddress }}' ):8000"; # run on host for open fromt page
