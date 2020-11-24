from django.db import models
# Create your models here.


class Student_Admission(models.Model):
    student_id = models.CharField('Student ID',max_length=200)
    student_age = models.IntegerField('Student Age')
    student_name = models.CharField('Student Name',max_length=150)
    student_email = models.EmailField('Student Email')
    student_amount = models.FloatField('Student Amount')
    student_address = models.TextField('Student Address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name
