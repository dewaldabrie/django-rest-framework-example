from __future__ import unicode_literals
import os
import subprocess
from django.core.management.base import BaseCommand, CommandError
from info.models import Company
import json

from paranuara_big_brother.settings import DB, MONGODB_DATABASES

class Command(BaseCommand):
    elp = """ Load an array of json objects into the db.
    Usage: 
    $ python manage.py load_companies <absolute-file-path> <database-name>
    """

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)
        parser.add_argument('database', type=str)

    def handle(self, *args, **options):
        # check that path is valid
        if not os.path.isfile(options['filepath']):
            raise CommandError('Invalid absolute file path.')

        # check database name is valid
        if options['database'] not in MONGODB_DATABASES.keys():
            raise CommandError('Invalid database name. Options are {}'.format(' and'.join(MONGODB_DATABASES.keys())))


        bulk = Company._get_collection().initialize_ordered_bulk_op()

        # read in json file
        # TODO: read this as a file stream with ijson to allow for arbitrary file size
        with open(options['filepath']) as f:
            company_records = json.load(f)
            for c in company_records:
                # do data cleaning
                # rename 'company' field to 'name'
                c['name'] = c['company']
                c.pop('company')
                # insert
                bulk.find({"index": c["index"]}).upsert().replace_one(c)
            # insert into database
            bulk.execute()

        self.stdout.write('Records inserted')
