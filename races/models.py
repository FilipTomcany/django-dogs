from django.db import models

# Create your models here.
class Race(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
