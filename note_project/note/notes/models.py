from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    pubTime = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField('Tag', related_name= 'notes')
    
    def __unicode__(self):
        return self.label
    
class Tag(models.Model):
    label = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.label