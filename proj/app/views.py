from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import ShortUrl
from .serializers import ShortUrlSerializer


# Create your views here.
class GetOriginalUrlView(generics.RetrieveAPIView):
    serializer_class = ShortUrlSerializer

    def get_object(self):
        return generics.get_object_or_404(
            ShortUrl.objects.all(), short_code=self.kwargs["short_code"]
        )

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        '''Increment count'''
        instance.count = instance.count + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GenerateShortUrlView(generics.CreateAPIView):
    serializer_class = ShortUrlSerializer


