from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from um_url_shortener.core.pregenerate_url.models import PregenerateUrl, PregenerateURLStatuses

import uuid


class Command(BaseCommand):
    # TODO: SHould be a cron job or if we meet a threshold then run this command, 100 is arbitrary
    help = 'Updates pregenerate table with 100 new urls'

    def handle(self, *args, **options):
        try:
            for _ in range(100):
                with transaction.atomic():
                    uid = uuid.uuid4()
                    PregenerateUrl.objects.create(
                        id=uid,
                        shorten_url_hash=str(uid)[:7],
                        status=PregenerateURLStatuses.inactive
                    )
            self.stdout.write(self.style.SUCCESS('Successfully generated URLs'))

        except Exception as e:
            raise CommandError(f'Error {e}')
