from datetime import datetime, timedelta
from celery.task import Task, PeriodicTask
from celery_demo.jobs.models import Current
import logging

logger = logging.getLogger('task')

class TimeTask(PeriodicTask):
    run_every = timedelta(seconds=10)

    def run(self):
        logger.info('TimeTask run...')
        current_time = str(datetime.now())
        c = Current.objects.create_from_date(current_time)
        c.save()
        logger.info('New current object')
        return True
        
