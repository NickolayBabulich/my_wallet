from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@shared_task(
    bind=True,
    max_retries=3,  # Максимальное количество повторов
    default_retry_delay=3600  # Повтор через час
)
def clean_inactive_user(self):
    try:
        day_ago = timezone.now() - timedelta(days=1)

        users = User.objects.filter(
            date_joined__lt=day_ago,
            last_login__isnull=True,
            is_active=False
        )

        for user in users:
            user.delete()
        return '--Deleted--'
    except Exception as e:
        return f'--Failed-- {str(e)}'
