from django.contrib import admin
from .models import OpenElective, Course, Response

# Register your models here.

admin.site.register(OpenElective)
admin.site.register(Course)
admin.site.register(Response)
