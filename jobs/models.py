from django.db import models
from celery_demo.jobs.manager import CurrentManager

class Current(models.Model):
    now = models.CharField(max_length=30, blank=True, null=True)
    objects = CurrentManager()
    
    def __unicode__(self):
        return '%s' % self.now
