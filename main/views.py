from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import OpenElective, Course, Response
from .serializers import OpenElectiveSerializer, CourseSerializer, ResponseSerializer, ResultSerializer

# Create your views here.

class OpenElectiveViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]
    queryset = OpenElective.objects.all()
    serializer_class = OpenElectiveSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = CourseSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ResultViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated ]

    serializer_class = ResultSerializer    