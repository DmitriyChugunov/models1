from django.db import models

class PostModel(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    image = models.ImageField(default='/static/alabuga2.jpg')