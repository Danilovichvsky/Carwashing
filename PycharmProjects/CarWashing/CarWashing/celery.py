
from __future__ import absolute_import
import os
from celery import Celery

from CarWashing import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarWashing.settings')


app = Celery("CarWashing",broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(['WetCar'])


