from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True)
    click_count = models.IntegerField(default=0)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=
    #         )
    #     ]
