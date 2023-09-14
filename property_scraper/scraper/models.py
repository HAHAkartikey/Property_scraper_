from django.db import models
# scraper/models.py
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.URLField()

    def __str__(self):
        return self.name
