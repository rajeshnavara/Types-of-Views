from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Student(TemplateView):
    template_name='Student.html'
    
class Employee(TemplateView):
    template_name='Employee.html'