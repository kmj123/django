from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student

def delete(request,name):
    render

# 학생정보 수정
def update(request,name):
    if request.method == "GET":
        print("삭제할 이름:",name)
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'students/update.html',context)
    else:
        print("test",name)
        return redirect('students/list/')

# 학생정보 상세보기
def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보 입력
def write(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보" ,name,major,grade,age,gender)
        Student(no=no,name=name,major=major,grade=grade,age=age,gender=gender).save() 
        return redirect('/students/list/')
    else: 
        return render(request,'students/write.html')

# 학생 정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'students/list.html',context)