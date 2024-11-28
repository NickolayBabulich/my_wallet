import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('config')

app.config_from_object('config.settings.dev', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clean_inactive_user': {
        'task': 'apps.account.tasks.clean_inactive_user',
        # 'schedule': crontab(minute='*/1'), # 1 минута - для отладки
        'schedule': crontab(hour=0, minute=0),  # Ежедневно в 00:00
        'args': (),
    },
}
