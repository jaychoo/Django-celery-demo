from django.contrib import admin
from celery_demo.jobs.models import Current


admin.site.register(Current)
