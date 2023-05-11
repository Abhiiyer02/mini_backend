import os
from django.db import models

BRANCH_CHOICES = [
        ("CSE","Coputer Science and Engineering"),
        ("ISE","Information Science Engineering"),
        ("ECE","Electronics and Communication Engineering"),
        ("CV","Civil Engineering"),
        ("ME","Mechanical Engineering"),
        ("EEE","Elcectrical and Electronics Engineering"),
        ("EI","Electronics and Instrumentation Engineering"),
        ("IP","Industrial Production"),
        ("CSBS","Computer Science and Business Systems Engineering"),
        ("CTM","Construction Technology Management"),
        ("PST","Polymer Sceince Engineering"),
        ("BT","BioTechnology Engineering"),
        ("EV","Environmental Engineering"),
        # ("","Engineering"),
    ]

# Create your models here.
def get_upload_path(instance, filename):
    return os.path.join('pdfs', str(instance.id), filename)

class OpenElective(models.Model):  
    name = models.CharField(max_length=20,primary_key=True)
    syllabus_pdf = models.FileField(upload_to=get_upload_path, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'  
    
class Course(models.Model):
    course_code = models.CharField(max_length=7,primary_key=True)
    branch = models.TextChoices(max_length=4, choices=BRANCH_CHOICES)
    course_name = models.TextField(max_length=30)
    maxCap = models.IntegerField(default=60)
    buffer = models.IntegerField(default=0)
    oe = models.ForeignKey(OpenElective, on_delete=models.CASCADE, default=None) 

    def __str__(self):
        return f'{self.course_code} - {self.course_name}'
        
        
# NOTE
# The idea was to make USN the primary key of responses but student was later inlcuded in the user models. 
# So whenever a student is submitting his/her preferneces , the USN ie the username/user_id is to be extracted from the api refesh/access token and is to be stored in the response table as the PK
class Response(models.Model):
    USN = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)
    sem = models.IntegerField()
    sec = models.CharField(max_length=1, null=True, blank=True)
    branch = models.TextChoices(max_length=4, choices=BRANCH_CHOICES)
    email = models.EmailField(unique=True)
    oe = models.ForeignKey(OpenElective, related_name='oe', on_delete=models.CASCADE)
    CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    pref1 = models.CharField(max_length=60)
    pref2 = models.CharField(max_length=60)
    pref3 = models.CharField(max_length=60)
    pref4 = models.CharField(max_length=60)
    pref5 = models.CharField(max_length=60)
    pref6 = models.CharField(max_length=60)
    pref7 = models.CharField(max_length=60)
    pref8 = models.CharField(max_length=60)
    pref9 = models.CharField(max_length=60)
    pref10 = models.CharField(max_length=60)
    alloted = models.CharField(max_length=60)
    
    def __str__(self):
        return self.USN , self.alloted
 
    
