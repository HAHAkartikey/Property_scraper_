from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from crontab.models import Job

class ScrapingRun(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    records_scraped = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="Pending")

class AdminSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cron_job_enabled = models.BooleanField(default=True)
    cron_job_schedule = models.CharField(max_length=50, default="0 8,20 * * *")
