from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.TextField(primary_key=True)
    image = models.FileField(upload_to='images/')
    tags = models.TextField(blank=True, null=True)
    poem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id