from django.db import models


class Order(models.Model):
    image = models.FileField(upload_to='')
    tags = models.TextField(null=True)
    poem = models.TextField(null=True)
    card = models.FileField(upload_to='card/', null=True)
