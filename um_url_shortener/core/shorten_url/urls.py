from django.urls import path

from um_url_shortener.core.shorten_url.views import ShortenURLViewSet

urlpatterns = [
    path('short_urls/', ShortenURLViewSet().short_urls)
]
