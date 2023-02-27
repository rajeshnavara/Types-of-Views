from django.shortcuts import render
from django.views.generic import FormView
from app.Forms import *
from django.http import HttpResponse
# Create your views here.

class Employee(FormView):
    template_name='Employee.html'
    form_class=Employee_form
    
    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))
    
class Student(FormView):
    template_name='Student.html'
    form_class=Student_form
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('Data Inserted Successfully')