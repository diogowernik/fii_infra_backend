
from django.core.management.base import BaseCommand
from django.core.management import call_command
from fi_infra.worker.worker import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        daily_scrap()
        # call_command('update')
        # call the worker
