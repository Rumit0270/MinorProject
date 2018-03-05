from django import forms

from django.forms import ModelForm
from . models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['user_name', 'gender','email', 'password']
        widgets = {
                    'password': forms.PasswordInput(),
                  }