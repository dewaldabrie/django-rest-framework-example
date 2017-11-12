Welcome to the REST API for the Paranuara colony
------------------------------------------------
This API will help the president of Paranuara find interesting information regarding his citizens.

Installation
````````````
1. Install MongoDB for your platform. Refer to the official installation instructions: https://docs.mongodb.com/manual/administration/install-on-linux/
2. Install Python 2.7 for your platform.
3. Install pip for Python2.7.
4. In your terminal, change to an appropriate directory and clone the github repository::

    $ git clone https://github.com/dewaldabrie/django-rest-framework-example.git
    $ cd django-rest-framework-example

5. Optionally create a virtual Python environment and::

    $ pip install -r requirements.txt


Loading data
````````````
The sample data can be loaded with a Django management command::

    $ cd site
    $ python manage.py load_companies "$PWD/info/data/companies.json" default
    $ python manage.py load_people "$PWD/info/data/people.json" default

The above scripts will also clean the data.

Starting up the server
----------------------
Make sure you're in the same directory as manage.py, then ::

    $ python manage.py runserver

Browse to localhost:8000/api

You can browse this api and interact with it or try the following urls:

* localhost:8000/api/company/1
* localhost:8000/api/person/0
* localhost:8000/api/person/0,1

