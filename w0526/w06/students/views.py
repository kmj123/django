from django.shortcuts import render
from students.models import Student

def  list(request):
    return render(request,'list.html')

