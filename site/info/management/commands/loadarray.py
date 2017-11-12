import os
import subprocess
from django.core.management.base import BaseCommand, CommandError
import info.models

from paranuara_big_brother.settings import DB, MONGODB_DATABASES

class Command(BaseCommand):
    help = """ Load an array of json objects into the db.
    Usage: 
    $ django-admin loadarray <name-of-collection> <absolute-file-path>
    """

    def add_arguments(self, parser):
        parser.add_argument('collection', type=str)
        parser.add_argument('filepath', type=str)
        parser.add_argument('database', type=str)

    def handle(self, *args, **options):
        # check that path is valid
        if not os.path.isfile(options['filepath']):
            raise CommandError('Invalid absolute file path.')

        # check that collection is valid
        if options['collection'].capitalize() not in dir(info.models):
            raise CommandError('Invalid collection name.')

        # check database name is valid
        if options['database'] not in MONGODB_DATABASES.keys():
            raise CommandError('Invalid database name. Options are {}'.format(' and'.join(MONGODB_DATABASES.keys())))

        # compile system command
        command_string = "mongoimport --jsonArray --host {host} --collection {collection} --file {file_path} --db {database}".format(
            host=MONGODB_DATABASES[DB]['host'],
            collection=options['collection'].lower(),
            file_path=options['filepath'],
            database=options['database'],
        )
        self.stdout.write('Calling: %s' % command_string)

        # call command
        process = subprocess.Popen(
            command_string,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        if out:
            self.stdout.write(out)
        if err:
            self.stderr.write(err)