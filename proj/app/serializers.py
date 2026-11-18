import secrets
import string

from rest_framework import serializers

from .models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['id', 'original_url', 'created_at', 'expire_at', "click_count"]
        read_only_fields = ['id', 'created_at', 'expire_at', "click_count"]

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits

        return ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

    def create(self, validated_data):
        code = self.generate_short_code()
        return ShortUrl.objects.create(
            original_url=validated_data['original_url'],
            short_code=code
        )





