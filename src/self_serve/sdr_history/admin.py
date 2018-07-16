from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Company)
admin.site.register(models.ReportSuite)
admin.site.register(models.Prop)
