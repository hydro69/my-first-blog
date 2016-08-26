from __future__ import unicode_literals

from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models

class Channel(models.Model):
    name = models.CharField(blank=False, max_length=100)
    def __unicode__(self):
        return self.name

class Link(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.URLField()
    created_on = models.DateTimeField(default=datetime.now())
    votes = models.IntegerField(default=0)
    channels = models.ManyToManyField(Channel)
    def __unicode__(self):
    return self.title
