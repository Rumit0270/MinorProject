from django.contrib import admin
from .models import Disease, Symptom, Patient, Doctor

# Register your models here.
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Patient)
admin.site.register(Doctor)


