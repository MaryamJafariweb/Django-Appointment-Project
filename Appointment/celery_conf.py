from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Appointment.settings')
celery_app = Celery('Appointment')
celery_app.autodiscover_tasks()