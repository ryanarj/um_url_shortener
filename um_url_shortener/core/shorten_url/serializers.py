import uuid

from django.db import transaction
from django.db.models import Q
from rest_framework import serializers

from um_url_shortener.core.pregenerate_url.models import PregenerateUrl, PregenerateURLStatuses
from um_url_shortener.core.shorten_url.models import ShortenUrl, ShortenURLStatuses


class CreateShortenSerializer(serializers.Serializer):
    original_url = serializers.CharField()

    def create(self, validated_data):
        original_url = validated_data.get('original_url')
        shorten_url_q = ShortenUrl.objects.filter(original_url=original_url)

        if not shorten_url_q.exists():
            pregenerate_url = PregenerateUrl.objects.filter(
                status=PregenerateURLStatuses.inactive
            ).order_by('created_at').first()

            with transaction.atomic():

                if not pregenerate_url:
                    uid = uuid.uuid4()
                    pregenerate_url = PregenerateUrl.objects.create(
                        id=uid,
                        shorten_url_hash=str(uid)[-7:],
                        status=PregenerateURLStatuses.inactive
                    )

                # TODO should be the name of a website, in a ENV variable
                shorten_url_str = f"http://127.0.0.1:8000/um/{pregenerate_url.shorten_url_hash}"
                shorten_url = ShortenUrl.objects.create(
                    original_url=original_url,
                    shorten_url=shorten_url_str,
                    status=ShortenURLStatuses.active,
                    pregenerate_url=pregenerate_url
                )
                pregenerate_url.status = PregenerateURLStatuses.active
                pregenerate_url.save()

            return shorten_url
        else:
            return shorten_url_q.first()
