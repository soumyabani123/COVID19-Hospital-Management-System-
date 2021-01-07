# Generated by Django 3.1.3 on 2020-12-18 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'covidproject_patient',
            },
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('ward_no', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_patients', models.IntegerField()),
                ('ward_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=20)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.patient')),
                ('ward_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.ward')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=20)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.patient')),
                ('ward_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.ward')),
            ],
        ),
        migrations.CreateModel(
            name='discharge_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discharge_date', models.DateField()),
                ('covid_status', models.CharField(max_length=20)),
                ('discharge_temp', models.IntegerField()),
                ('discharge_symptoms', models.CharField(max_length=30)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.patient')),
            ],
        ),
        migrations.CreateModel(
            name='admit_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admit_date', models.DateField()),
                ('covid_status', models.CharField(max_length=20)),
                ('admit_temp', models.IntegerField()),
                ('admit_symptoms', models.CharField(max_length=30)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidproject.patient')),
            ],
        ),
    ]