from django.db import models

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
