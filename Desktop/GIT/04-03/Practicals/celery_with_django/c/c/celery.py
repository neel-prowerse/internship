import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','c.settings')
app = Celery('c')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule =    {
                                'add-every-30-seconds': {
                                                            'task':'app.tasks.add_numbers',
                                                            'schedule':30.0,
                                                            'args':(1,2)
                                                        }
                            }
