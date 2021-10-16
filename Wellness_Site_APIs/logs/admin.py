from django.contrib import admin
from logs.models import DietLog, WorkoutLog

# Register your models here.
admin.site.register(DietLog)
admin.site.register(WorkoutLog)