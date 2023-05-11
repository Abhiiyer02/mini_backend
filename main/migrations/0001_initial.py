# Generated by Django 4.2.1 on 2023-05-11 16:34

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenElective',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('syllabus_pdf', models.FileField(blank=True, default=None, null=True, upload_to=main.models.get_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('USN', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sem', models.IntegerField()),
                ('sec', models.CharField(blank=True, max_length=1, null=True)),
                ('branch', models.CharField(choices=[('CSE', 'Coputer Science and Engineering'), ('ISE', 'Information Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CV', 'Civil Engineering'), ('ME', 'Mechanical Engineering'), ('EEE', 'Elcectrical and Electronics Engineering'), ('EI', 'Electronics and Instrumentation Engineering'), ('IP', 'Industrial Production'), ('CSBS', 'Computer Science and Business Systems Engineering'), ('CTM', 'Construction Technology Management'), ('PST', 'Polymer Sceince Engineering'), ('BT', 'BioTechnology Engineering'), ('EV', 'Environmental Engineering')], max_length=4)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pref1', models.CharField(max_length=60)),
                ('pref2', models.CharField(max_length=60)),
                ('pref3', models.CharField(max_length=60)),
                ('pref4', models.CharField(max_length=60)),
                ('pref5', models.CharField(max_length=60)),
                ('pref6', models.CharField(max_length=60)),
                ('pref7', models.CharField(max_length=60)),
                ('pref8', models.CharField(max_length=60)),
                ('pref9', models.CharField(max_length=60)),
                ('pref10', models.CharField(max_length=60)),
                ('alloted', models.CharField(max_length=60)),
                ('oe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oe', to='main.openelective')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('branch', models.CharField(choices=[('CSE', 'Coputer Science and Engineering'), ('ISE', 'Information Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CV', 'Civil Engineering'), ('ME', 'Mechanical Engineering'), ('EEE', 'Elcectrical and Electronics Engineering'), ('EI', 'Electronics and Instrumentation Engineering'), ('IP', 'Industrial Production'), ('CSBS', 'Computer Science and Business Systems Engineering'), ('CTM', 'Construction Technology Management'), ('PST', 'Polymer Sceince Engineering'), ('BT', 'BioTechnology Engineering'), ('EV', 'Environmental Engineering')], max_length=4)),
                ('course_name', models.TextField(max_length=30)),
                ('maxCap', models.IntegerField(default=60)),
                ('buffer', models.IntegerField(default=0)),
                ('oe', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.openelective')),
            ],
        ),
    ]