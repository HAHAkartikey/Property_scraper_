from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ScrapingRun, AdminSettings

admin.site.register(ScrapingRun)
admin.site.register(AdminSettings)

