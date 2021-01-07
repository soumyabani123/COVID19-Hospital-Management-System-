from django.contrib import admin
from .models import patient
from .models import ward
from .models import doctor
from .models import admit_info
from .models import discharge_info
from .models import staff
# Register your models here.



admin.site.register(patient)
admin.site.register(ward)
admin.site.register(doctor)
admin.site.register(admit_info)
admin.site.register(discharge_info)
admin.site.register(staff)

