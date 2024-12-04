from django.db import models
from tinymce.models import HTMLField


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = HTMLField()
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name