import uuid

from django.db import models


class PregenerateURLStatuses:
    inactive = "inactive"
    active = "active"

    PREGENERATE_URL_CHOICES = (
        ("INACTIVE", "inactive"),
        ("ACTIVE", "active"),
    )


class PregenerateUrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    shorten_url_hash = models.CharField(max_length=7)
    status = models.CharField(max_length=10, choices=PregenerateURLStatuses.PREGENERATE_URL_CHOICES, default="inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



