from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import ScrapingRun, AdminSettings
from crontab.models import Job

def admin_dashboard(request):
    # Retrieve scraping run history
    scraping_runs = ScrapingRun.objects.all().order_by('-timestamp')

    # Retrieve admin settings
    admin_settings = AdminSettings.objects.get(user=request.user)

    # Retrieve the status of the cron job
    cron_job_status = Job.objects.filter(command="python manage.py scrape_property_data").exists()

    context = {
        'scraping_runs': scraping_runs,
        'admin_settings': admin_settings,
        'cron_job_status': cron_job_status,
    }

    return render(request, 'admin_interface/dashboard.html', context)


