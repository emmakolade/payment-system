from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payment.settings')

app = Celery('payment')

app.config_from_object(settings, namespace='CELERY')

#TODO: celery beat settings
app.conf.beat_schedule = {
    'charge-cards-every-2-minutes':{
        'task': 'testpay.tasks.charge_card',
        'schedule': crontab(minute='*/2'),
    },
}

app.autodiscover_tasks()
app.conf.timezone = 'UTC'

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}') 