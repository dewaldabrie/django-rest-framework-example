FROM mongo:3.5

MAINTAINER dewaldabrie

ENV PYTHONUNBUFFERED 1

# Install base packages
RUN set -x && \
    apt-get update && \
    apt-get install -y python python-pip git

# Install Django App
RUN git clone https://github.com/dewaldabrie/django-rest-framework-example.git paranuara_surveillance
WORKDIR paranuara_surveillance
RUN pip install -r requirements.txt

# Database Migration
WORKDIR /paranuara_surveillance/site
RUN python manage.py migrate
# Load data into MongoDB
RUN python manage.py load_companies "$PWD/info/data/companies.json" default && \
    python manage.py load_people "$PWD/info/data/people.json" default

# Setup UWSGI
CMD ["uwsgi", "--module=paranuara_surveillance.site.wsgi:application", "--env=DJANGO_SETTINGS_MODULE=paranuara_surveillance.site.settings", "--master", "--pidfile=/tmp/par_surv.pid", "--http=0.0.0.0:8000", "--socket=0.0.0.0:8001", "--buffer-size=32768"]

EXPOSE 8000