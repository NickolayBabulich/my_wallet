from django.core.management import BaseCommand
from apps.account.tasks import clean_inactive_user


class Command(BaseCommand):
    def handle(self, *args, **options):
        result = clean_inactive_user.delay(2, 1)
        self.stdout.write(
            self.style.SUCCESS(f'Task {result.id} has been scheduled')
        )