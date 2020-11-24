from .models import Student_Admission
from rest_framework import serializers


class StudentAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Admission
        fields = ['id','student_id', 'student_age', 'student_name', 'student_email', 'student_amount', 'student_address']