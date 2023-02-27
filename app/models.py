from django.db import models

# Create your models here.
class Student(models.Model):
    Sid=models.IntegerField()
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Saddress=models.TextField()
    Scontact=models.IntegerField()
    
    def __str__(self):
        return self.Sname