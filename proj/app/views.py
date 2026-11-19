from django.db.models import F
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from .models import ShortUrl
from .serializers import ShortUrlSerializer


# Create your views here.
class RedirectToOriginalUrlView(generics.RetrieveAPIView):
    serializer_class = ShortUrlSerializer

    def get_object(self):
        return generics.get_object_or_404(
            ShortUrl.objects.all(), short_code=self.kwargs["short_code"]
        )

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.expire_at and instance.expire_at <= timezone.now():
            return Response(
                {"detail": "This short URL has expired."},
                status=status.HTTP_410_GONE
            )

        ShortUrl.objects.filter(pk=instance.pk).update(click_count=F('click_count')+1)
        return redirect(instance.original_url)


class GenerateShortUrlView(generics.CreateAPIView):
    serializer_class = ShortUrlSerializer


