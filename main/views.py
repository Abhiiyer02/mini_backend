from django.shortcuts import render
from rest_framework import viewsets

from .models import OpenElective, Course, Response
from .serializers import OpenElectiveSerializer, CourseSerializer, ResponseSerializer, ResultSerializer

# Create your views here.

class OpenElectiveViewSet(viewsets.ModelViewSet):
    permission_classes = [ ]
    queryset = OpenElective.objects.all()
    serializer_class = OpenElectiveSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [ ]
    serializer_class = CourseSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = [ ]
    queryset = Response.objects.all()