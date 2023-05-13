from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http import JsonResponse
from django.views import View
from .models import OpenElective, Course, Response
from .serializers import OpenElectiveSerializer, CourseSerializer, ResponseSerializer, ResultSerializer

# Create your views here.

class OpenElectiveViewSet(viewsets.ModelViewSet):
    # permission_classes = [ permissions.IsAuthenticated ]
    queryset = OpenElective.objects.all()
    serializer_class = OpenElectiveSerializer

class IsValidOpenElective(permissions.BasePermission):
    def has_permission(self, request, view):
        oe_name = request.path.split('/')[2]
        if not OpenElective.objects.filter(name=oe_name).exists():
            return False
        return True

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsValidOpenElective ]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        oe_name = self.request.path.split('/')[2]
        if oe_name is not None:
            queryset = queryset.filter(oe=oe_name)
        return queryset

class ResponseViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsValidOpenElective ]
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        oe_name = self.request.path.split('/')[2]
        if oe_name is not None:
            queryset = queryset.filter(oe=oe_name)
        return queryset

class ResultViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsValidOpenElective ]
    queryset = Response.objects.all()
    serializer_class = ResultSerializer   

    def get_queryset(self):
        queryset = super().get_queryset()
        oe_name = self.request.path.split('/')[2]
        if oe_name is not None:
            queryset = queryset.filter(oe=oe_name)
        return queryset


class AllotView(View):
    
    students = Response.objects.all()
    courses = Course.objects.all()
    

    def get_queryset(self):
        oe_name = self.request.path.split('/')[2]
        self.students = Response.objects.filter(oe=oe_name)
        self.courses = Course.objects.filter(oe=oe_name)

    
    def createStud(self):
        for student in self.students:
            choice=[]
            for j in range(2,19):
                val=studs.cell(i,j).value
                #print(val)
                if j ==2:
                    email=val
                elif j ==3:
                    usn = val
                elif j ==4:
                    sname = val
                elif j ==5:
                    #print(i,j)
                    cgpa = float(val)
                elif j==6:
                    sem=val
                elif j ==7 :
                    sec=val      
                elif j ==8 :
                    sbranch = val
                else:
                    if val != None:
                        val=val.split(': ')[0]
                        choice.append(val)#val[0:-1]
            s=Student(sname,sem,sec,usn,email,cgpa,sbranch,choice)
            Studs.append(s)
        


    def post(self, request, *args, **kwargs):

    # Perform the relevant code to allot students to courses
        for student in self.students :
            preferred_courses = [student.pref1,student.pref1,student.pref2,student.pref3,student.pref4,student.pref5,student.pref6,student.pref7,student.pref8,student.pref9,student.pref10]
            for i in range(self.students.count()):
                reallot= -1
                reallot=AllotCourse(Studs[i],i)
                while reallot > 0 :
                student[reallot].alloc=""
                    reallot=AllotCourse(Studs[reallot],reallot)

        # Store the results in your database
        for course in self.courses:
            course.save()

        # Return a JSON response with the results
        return JsonResponse({'success':True})