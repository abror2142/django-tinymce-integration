from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    desc = HTMLField()

    def __str__(self):
        return self.name