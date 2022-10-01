import uuid

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from um_url_shortener.core.shorten_url.models import ShortenUrl
from um_url_shortener.core.pregenerate_url.models import PregenerateUrl
from um_url_shortener.core.shorten_url.views import ShortenURLViewSet


class ShortenURLTestCase(TestCase):

    def test_new_url(self):
        factory = APIRequestFactory()

        # Test variables
        original_url = 'https://unitedmasters.com/'
        uid = uuid.uuid4()

        # Create a pregen url
        pregenerate_url = PregenerateUrl.objects.create(
            id=uid,
            shorten_url_hash=str(uid)[:7]
        )

        # Send request
        request = factory.post('/short_urls/', {
            'original_url': original_url
        }, format='json')

        # Get response
        response = ShortenURLViewSet().short_urls(request)

        # Assert
        shorten_url_str = f"http://127.0.0.1:8000/um/{pregenerate_url.shorten_url_hash}"
        shorten_url = ShortenUrl.objects.filter(original_url=original_url, shorten_url=shorten_url_str)

        assert shorten_url.exists() is True
        assert shorten_url.count() == 1
        assert shorten_url.first().shorten_url == shorten_url_str
        assert response.status_code == 201

    def test_original_url(self):
        factory = APIRequestFactory()

        # Test variables
        original_url = 'https://unitedmasters.com/'
        uid = uuid.uuid4()

        # Create a pregen url
        pregenerate_url = PregenerateUrl.objects.create(
            id=uid,
            shorten_url_hash=str(uid)[:7]
        )

        # Send request
        request = factory.post('/short_urls/', {
            'original_url': original_url
            }, format='json'
        )
        ShortenURLViewSet().short_urls(request)

        shorten_url_str = f"http://127.0.0.1:8000/um/{pregenerate_url.shorten_url_hash}"
        # Send request
        request = factory.get(
            f'/short_urls?shorten_url={shorten_url_str}',
            format='json'
        )
        res = ShortenURLViewSet().short_urls(request)

        # Assert
        assert res.status_code == 200
