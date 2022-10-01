from django.db import models

from um_url_shortener.core.pregenerate_url.models import PregenerateUrl


class ShortenURLStatuses:
    inactive = "inactive"
    active = "active"
    expired = "expired"

    SHORTEN_URL_CHOICES = (
        ("INACTIVE", "inactive"),
        ("ACTIVE", "active"),
        ("EXPIRED", "expired"),
    )

class ShortenUrl(models.Model):
    original_url = models.TextField()
    shorten_url = models.CharField(max_length=25)
    status = models.CharField(max_length=10, choices=ShortenURLStatuses.SHORTEN_URL_CHOICES, default="inactive")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pregenerate_url = models.ForeignKey(PregenerateUrl, on_delete=models.CASCADE)



