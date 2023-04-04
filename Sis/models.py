from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    email = models.EmailField()
    seat = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name}'
