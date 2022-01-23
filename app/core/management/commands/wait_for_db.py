import time
from psycopg2 import OperationalError as Psycopyg2OpError
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to stop execution until Database is accessible"""
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write('Waiting for database ...')
        db_conn = None
        while not db_conn:
            try:
                db_conn=connections['default']
            except (OperationalError, Psycopyg2OpError):
                self.stdout('DB unavailable, waiting for 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available !!!'))