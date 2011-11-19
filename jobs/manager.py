from django.db import models

class CurrentManager(models.Manager):

    def create_from_date(self, date):
        return self.create(now=date)
    
