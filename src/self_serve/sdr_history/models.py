from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

class ReportSuite(models.Model):
    site_name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )

class Prop(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    enabled = models.BooleanField()
    report_suite = models.ForeignKey(
        'ReportSuite',
        on_delete=models.CASCADE,
    )

#class Evars(models.Model):


#class ConfigVersions(models.Model):


#class ConfigChanges(models.Model):
