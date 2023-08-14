from django.db import models

# Create your models here.
class Exercise(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(default='')
    experience = models.IntegerField(default=0)

    