from django.test import TestCase
from datetime import datetime, timedelta
from api.models import Level, Origin, Environment, Log
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

 class TestProject(TestCase):
     def setup(self) -> None:
        ocorrencia = Log.objects.create(details='teste', title='Ocorrencia', number_events=1, occurrence_date=datetime.today(),
                                   active=1)
         Level.objects.create(description='DEBUG"')
         Environment.objects.create(description='teste')
         Origin.objects.create(description='teste')
#
#     def test_Level(self):
#         level = Level.objects.get(description='DEBUG')
#         self.assertEqual(level.title,'DEBUG')
#
#     def test_Log(self):
#         ocorrencia = Log.objects.get(title='Ocorrencia')
#         self.assertEqual(log.title,'Ocorrencia')