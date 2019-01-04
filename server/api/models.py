from django.db import models


class Order(models.Model):
    image = models.FileField(upload_to='')
    type = models.TextField(choices=(('portrait', 'portrait'), ('landscape', 'landscape')), default='landscape')
    tags = models.TextField(null=True)
    couplet_viewed = models.IntegerField(default=0)
    poem_viewed = models.IntegerField(default=0)

class Couplet(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    index = models.IntegerField(help_text='start with 1')
    content = models.TextField()
    card = models.FileField(upload_to='couplet/')

class Poem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    index = models.IntegerField(help_text='start with 1')
    content = models.TextField()
    card = models.FileField(upload_to='poem/') 
