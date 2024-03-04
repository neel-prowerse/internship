# Commands We have to execute  : 
1. First go to dir (cd )

2. Make virtual environment (python -m venv (nameenv) ).

3.  Now Activate virtual environment using (source nameenv/bin/activate).

4. Install Django (pip install django)

5. Start Project in Django (python  -m django startproject pro_name)

6. cd pro_name

7. pip install "celery[redis]"

8. go to settings.py
import os 
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangocelery.settings')
# set the default Django settings module for the 'celery' program.
app = Celery('djangocelery',backend='redis',broker='redis://localhost:6379')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

9. djangocelery/init.py : 
from __future__ import absolute_import, unicode_literals
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
__all__ = ('celery_app',)

10. go to settings.py
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

INSTALLED_APPS = [
    # others app
    'celery',

]

11. python manage.py startapp main

12. Create a tasks.py in main app
# mysite/main/tasks.py

from __future__ import absolute_import
from celery import shared_task


@shared_task
def test(param):
    return 'The tasks executed with the following parameter: "%s" '

13. create a urls.py in the main app
# mysite/main/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ),
]

14. Add a view to connect the newly added task to a slug.  Notice how we add delay when we call the task to execute the function in the background.
# mysite/main/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test

# Create your views here.
def home(request):
  test.delay(15)
  return HttpResponse("Hey there!")

15. # On Mac, feel free to use Homebrew and enter the following commands in the djangocelery directory
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
$ brew 
# brew install redis
# Run redis-server in terminal
# In a new terminal, go to the project directory and run redis-client
# Type in "ping" and you should receive a "PONG" response
# Keep your Redis server running in one terminal/command prompt, in the other, stop running redis-client and enter the following command to install flower

16. pip install flower

17. Now, make sure to have 4 terminals/command prompts for the following commands:
1) To run the redis server 
2) To run: py/python3 manage.py runserver
3) To run celery: celery -A mysite worker -l info --pool=solo
4) To run flower: flower -A mysite
After running flower, you will see an address to view the dashboard, in this case, at port 5555
