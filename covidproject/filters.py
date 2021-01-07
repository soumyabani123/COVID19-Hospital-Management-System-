from .models import patient
from .models import doctor
from .models import staff
from .models import admit_info

import django_filters

class patientfilter(django_filters.FilterSet):
    class Meta:
        model = patient
        fields = '__all__'

class doctorfilter(django_filters.FilterSet):
    class Meta:
        model = doctor
        fields = '__all__'
        exclude = 'patient_id'

class stafffilter(django_filters.FilterSet):
    class Meta:
        model = staff
        fields = '__all__'
        exclude = 'patient_id'

class admitfilter(django_filters.FilterSet):
    class Meta:
        model = admit_info
        fields = {'covid_status'}

