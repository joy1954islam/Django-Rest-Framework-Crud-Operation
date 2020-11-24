from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student_Admission
from .serializers import StudentAdmissionSerializer


@csrf_exempt
def student_list(request):
    """
    List all code snippets, or create a new Student Admission.
    """
    if request.method == 'GET':
        students = Student_Admission.objects.all()
        serializer = StudentAdmissionSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentAdmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        student = Student_Admission.objects.get(pk=pk)
    except student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentAdmissionSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentAdmissionSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)