from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name