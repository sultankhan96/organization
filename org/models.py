from django.conf import settings
from django.db import models
from django.utils import timezone


class Worker(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Position(models.Model):
    title = models.CharField(max_length=200)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return self.title
