from django.urls import path

from FBV.views import student_list,student_detail

urlpatterns = [
    path('student_list/', student_list,name='student_list'),
    path('student_list/<int:pk>/', student_detail,name='student_update'),
]