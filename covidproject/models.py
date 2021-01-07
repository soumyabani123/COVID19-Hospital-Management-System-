from django.db import models


class patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    def __str__(self):
        return self.patient_name
    class Meta:
        db_table="covidproject_patient"
    


class ward(models.Model):
    ward_no=models.AutoField(primary_key=True)
    no_of_patients=models.IntegerField()
    ward_phone=models.IntegerField()
    def __str__(self):
        return str(self.ward_no)


class doctor(models.Model):
    doc_id=models.AutoField(primary_key=True)
    doc_name=models.CharField(max_length=20)
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    ward_no=models.ForeignKey(ward,on_delete=models.CASCADE)
    def __str__(self):
        return self.doc_name
    


class admit_info(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    admit_date=models.DateField(auto_now=False)
    covid_status=models.CharField(max_length=20)
    admit_temp=models.IntegerField()
    admit_symptoms=models.CharField(max_length=30)
    

class discharge_info(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    discharge_date=models.DateField(auto_now=False)
    covid_status=models.CharField(max_length=20)
    discharge_temp=models.IntegerField()
    discharge_symptoms=models.CharField(max_length=30)
    

class staff(models.Model):
    staff_id=models.AutoField(primary_key=True)
    staff_name=models.CharField(max_length=20)
    ward_no=models.ForeignKey(ward,on_delete=models.CASCADE)
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    def __str__(self):
        return self.staff_name



    