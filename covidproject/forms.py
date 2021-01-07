from django import forms
from .models import patient

class patientform(forms.ModelForm):
    patient_name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    address = forms.CharField()
    
    class Meta:
        model=patient
        fields = ('patient_name','age','gender','address')