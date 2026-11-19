from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['short_code'],
                name='unique_short_code'
            )
        ]