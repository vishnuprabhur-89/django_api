from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from app.models import Student, Subject
from app.serializers import StudentSerializer, SubjectSerializer
from rest_framework.decorators import api_view
from django.db.models import Sum
from datetime import datetime
import math

class StudentView(generics.GenericAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        student_obj = Student.objects.all()
        total_student = student_obj.count()
        if search_param:
            stud_details = student_obj.filter(title__icontains=search_param)
        serializer = self.serializer_class(student_obj[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_student,
            "page": page_num,
            "limit": limit_num,
            "last_page": math.ceil(total_student / limit_num),
            "students": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": dict.fromkeys(list(serializer.errors), serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

class SubjectView(generics.GenericAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    student_query = Student.objects.all()
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        search_type = request.GET.get("searchType")
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        if search_type == "student":
            list_subject = Subject.objects.values('studentRollNo', 'student_name', 'english', 'science', 'maths', 'computer', 'social')
        elif search_type == "totalmarks":
            list_subject = Subject.objects.values('studentRollNo', 'student_name', 'total_marks')
        else:
            list_subject = Subject.objects.all()
        total_subj = list_subject.count()
        if search_param:
            subj = list_subject.filter(title__icontains=search_param)
        serializer = self.serializer_class(list_subject[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_subj,
            "page": page_num,
            "limit": limit_num,
            "last_page": math.ceil(total_subj / limit_num),
            "students": serializer.data
        })

    def post(self, request):
        if request.data:
            studentId = request.data.get('studentRollNo')
            if studentId is not None:
                try:
                    isValid = Student.objects.get(rollNo=studentId)
                    serializer = self.serializer_class(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "Subject wise marks are added.", "message": serializer.data}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                except Student.DoesNotExist:
                    return Response({"status": "fail", "message": "Given student roll no does not exists"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": "fail", "message": "Student roll no is missing"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "fail", "message": "Required inputs are missing"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_average_marks(request):
    queryset = Subject.objects.all()
    total_count = queryset.count()
    list_subject = Subject.objects.aggregate(Sum('english'), Sum('maths'), Sum('science'), Sum('computer'), Sum('social'))
    subject_averages = {i: ("%.2f" % (list_subject[i]/total_count)) for i in list_subject.keys()}
    return Response({"status": "success", "total_students": total_count, "subject_wise_average_marks": subject_averages})

