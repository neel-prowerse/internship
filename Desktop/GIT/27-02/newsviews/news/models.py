from django.db import models

# Create your models here.
class News(models.Model):
    headlines = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    date = models.DateField()
