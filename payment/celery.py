import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payment.settings')

app = Celery('payment')
app.config_from_object('django.conf:settings', namespace='CELERY')
# 
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'charge-wallet-every-2-minutes': {
        'task': 'testpay.tasks.charge_wallet',
        'schedule': crontab(minute='*/2'),  # every 2 minutes
    },
}








# # from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from celery.schedules import crontab
# from django.conf import settings
# from datetime import timedelta


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payment.settings')

# app = Celery('payment')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()
# # TODO: celery beat settings
# app.conf.beat_schedule = {
#     'process-payment-every-2-minutes': {
#         'task': 'testpay.tasks.process_payment',
#         'schedule': crontab(minute='*/2'),
#         # 'schedule': timedelta(minutes=2),
#     },
# }

# app.conf.timezone = 'UTC'

# # @app.task(bind=True)
# # def debug_task(self):
# #     print(f'Request: {self.request!r}')


