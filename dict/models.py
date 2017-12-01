# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Entry(models.Model):
    editor = models.ForeignKey('auth.User')
    word = models.CharField(max_length=100)
    status = models.CharField(max_length=15)
    category = models.CharField(max_length=10) 
    pos = models.CharField(max_length=10) 
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.word
