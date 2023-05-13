from rest_framework import serializers
from .models import OpenElective, Course, Response

class OpenElectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenElective
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_code',
            'course_name',
            'branch',
            'maxCap',
        )

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = (
            'USN',
            'name',
            'sem',
            'sec',
            'branch',
            'email',
            'CGPA',
            'pref1', 'pref2', 'pref3', 'pref4', 'pref5', 'pref6', 'pref7', 'pref8', 'pref9', 'pref10',
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = (
            'USN',
            'name',
            'sem',
            'sec',
            'branch'
            'CGPA',
            'pref1', 'pref2', 'pref3', 'pref4', 'pref5', 'pref6', 'pref7', 'pref8', 'pref9', 'pref10',
            'alloted',
        )