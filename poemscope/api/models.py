from django.db import models


class Order(models.Model):
    id = models.IntegerField(name='id', primary_key=True)
    image = models.FileField(name='image', upload_to='../images/')
    tags = models.CharField(name='tags', max_length=1000, null=True)
    poem = models.CharField(name='poem',max_length=1000, null=True)
