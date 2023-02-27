from django import forms
from .models import *
# Write your forms here

class Employee_form(forms.Form):
    Eid=forms.IntegerField()
    Ename=forms.CharField(max_length=100)
    Eemail=forms.EmailField()


class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'