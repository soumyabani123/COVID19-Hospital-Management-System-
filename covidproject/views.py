from django.shortcuts import render
from django.contrib import messages
from django.db import connection
#from django.http import HttpResponse
from .filters import patientfilter
from .models import patient
from .models import doctor
from .models import ward
from .models import staff
from .models import admit_info
from .models import discharge_info
from .filters import doctorfilter
from .filters import stafffilter
from .filters import admitfilter

# Create your views here.

def home(request):

    return render(request,'user/home.html')

def login(request):
    return render(request,'user/login.html')

def patient_details(request):
    #if request.method=="POST":
    #    gender=request.POST.get('gender')
    #    with connection.cursor() as cursor:
    #        cursor.callproc('patinfo',params=gender)
            
    #    has_contacted = patient.objects.all().filter(gender=gender)
    #    return render(request,'user/Patient.html')

    #if request.method=="POST":
    #    gender=request.POST.get('gender')
    #    showsearch=patient.objects.raw("CALL patinfo('"+gender+"')")
    #    return render(request,'user/patient.html',{'Data':showsearch})
    #else:
     #   showsrch=patient.objects.raw('select patient_id,patient_name,age,gender,address from covidproject_patient')
      #  return render(request,'user/patient.html',{'Data':showsrch})
      
    covidproject = patient.objects
    myfilter = patientfilter(request.GET, queryset=covidproject)
    covidproject = myfilter.qs
    context={'covidproject':covidproject,'myfilter':myfilter}
    return render(request,'user/Patient.html',context)

def doctor_details(request):
    #if request.method=="POST":
    #    ward_no=request.POST.get('ward_no')
    #    showsearch=doctor.objects.raw("CALL doctordetails('"+str(ward_no)+"')")
    #    return render(request,'user/doctor.html',{'Data':showsearch})
    
    covidproject = doctor.objects
    myfilter = doctorfilter(request.GET, queryset=covidproject)
    covidproject = myfilter.qs
    context={'covidproject':covidproject,'myfilter':myfilter}
    return render(request,'user/doctor.html',context)

def ward_details(request):
    covidproject = ward.objects
    return render(request,'user/ward.html',{'covidproject':covidproject})

def staff_details(request):
    
    covidproject = staff.objects
    myfilter = stafffilter(request.GET, queryset=covidproject)
    covidproject = myfilter.qs
    context={'covidproject':covidproject,'myfilter':myfilter}
    return render(request,'user/staff.html',context)

def admit_info_details(request):
    covidproject = admit_info.objects.order_by('-admit_date')
    myfilter = admitfilter(request.GET, queryset=covidproject)
    covidproject = myfilter.qs
    context={'covidproject':covidproject,'myfilter':myfilter}
    return render(request,'user/admit_info.html',context)

def discharge_info_details(request):
    covidproject = discharge_info.objects.order_by('-discharge_date')
    return render(request,'user/discharge_info.html',{'covidproject':covidproject})

def addpatient(request):
        patient1=patient()
        #mydict={'patient_name':patient.patient_name,
        #        'age':patient.age,
        #        'gender':patient.gender,
        #        'address':patient.address,
        #       }
        
        if request.method == 'POST':
            
            if request.POST.get('patient_name') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('address'):
                
                patient1.patient_name= request.POST.get('patient_name')
                patient1.age= request.POST.get('age')
                patient1.gender= request.POST.get('gender')
                patient1.address= request.POST.get('address')
                patient1.save()
                messages.success(request,'Record Saved Successfully...!')
                
        return render(request, 'user/addpatient.html',{'patient':patient1})  
         
#def search(request):
#    patient_list = patient.objects.all()
#    patient_filter = patientfilter(request.GET, queryset=patient_list)
#    return render(request,'search/patientfilter.html',{'filter':patient_filter})
#def my_custom_sql(self):
#    with connection.cursor() as cursor:
#        cursor.callproc('patinfo', ['M'])

    








                