from django.contrib import admin
from logs.models import DietLog, WorkoutLog,HealthData

# Register your models here.
admin.site.register(DietLog)
admin.site.register(WorkoutLog)
admin.site.register(HealthData)