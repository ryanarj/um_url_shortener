from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.core.cache import cache
from rest_framework.throttling import AnonRateThrottle

from um_url_shortener.core.shorten_url.models import ShortenUrl
from um_url_shortener.core.shorten_url.serializers import CreateShortenSerializer


class ShortenURLViewSet(viewsets.ModelViewSet):

    throttle_classes = [AnonRateThrottle]

    @staticmethod
    @csrf_exempt
    def short_urls(request: WSGIRequest) -> Optional[JsonResponse]:

        if request.method == 'POST':
            print(request)
            data = JSONParser().parse(request)
            serializer = CreateShortenSerializer(data=data)
            if serializer and serializer.is_valid():
                url = serializer.save()
                data = {'shorten_url': url.shorten_url}
                return JsonResponse(data, status=201)
            return JsonResponse(serializer.errors, status=400)

        if request.method == 'GET':
            shorten_url_str: Optional[str] = request.GET.get('shorten_url')
            shorten_url_data: Optional[dict] = cache.get(shorten_url_str)

            if shorten_url_data is None:
                # Parse for uuid
                clean_shorten_url_str = shorten_url_str.split("/")[-1]
                shorten_url_q = ShortenUrl.objects.filter(
                    Q(shorten_url=shorten_url_str) | Q(pregenerate_url__shorten_url_hash=clean_shorten_url_str)
                )

                if shorten_url_q.exists():
                    short_url_obj = shorten_url_q.first()
                    data = {'original_url': short_url_obj.original_url}
                    cache.set(shorten_url_str, data)
                    return JsonResponse(data, safe=False)
                else:
                    return JsonResponse(data={'error': 'Original url Not found'}, safe=False, status=404)
            else:
                return JsonResponse(shorten_url_data, safe=False)