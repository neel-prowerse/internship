from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    subject = models.TextField()
    def __str__(self):
        return self.name
    