from django.shortcuts import render,redirect
from students.models import Student

# 상세보기
def view(request,name):
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생 등록 저장
def writeOk(request):
    no = request.POST.get('no')
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    
    print(no,name,major,grade,age,gender,hobby)
    
    Student(no,name,major,grade,age,gender,hobby).save()
    return redirect('/students/list/')

# 학생 등록 화면
def write(request):
    return render(request,'students/write.html')

# 학생 전체 리스트
def list(request):
    qs = Student.objects.all()
    context= {'list':qs}
    return render(request,'students/list.html',context)
