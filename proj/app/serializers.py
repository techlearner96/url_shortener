from django.db import transaction, IntegrityError
from rest_framework import serializers

from .models import ShortUrl
from .utils import generate_short_code


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['id', 'short_code', 'original_url', 'created_at', 'expire_at', "click_count"]
        read_only_fields = ['id', 'created_at', "click_count", 'short_code']

    def create(self, validated_data):
        max_retries = 3

        for attempt in range(max_retries):
            code = generate_short_code()

            try:
                with transaction.atomic():
                    return ShortUrl.objects.create(
                        original_url=validated_data['original_url'],
                        short_code=code,
                        expire_at=validated_data.get('expire_at')
                    )

            except IntegrityError as exc:
                constraint_name = getattr(
                    getattr(exc.__cause__, 'diag', None),
                    'constraint_name',
                    None
                )

                if constraint_name != 'unique_short_code':
                    raise

                if attempt == max_retries - 1:
                    raise serializers.ValidationError(
                        "Unable to generate a unique short code."
                    )





