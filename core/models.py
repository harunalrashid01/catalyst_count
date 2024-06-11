from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=100)
    size_range = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linkedin_url = models.URLField(max_length=200)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()

    def __str__(self):
        return self.name
    
class file(models.Model):
#   date_uploaded = models.DateTimeField(auto_now=True)
  csv_file = models.FileField(upload_to='files')    
