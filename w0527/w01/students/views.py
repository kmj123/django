from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student
from django.urls import reverse

# 학생정보 리스트
def list(request):
    # Student 테이블 가져오기
    qs = Student.objects.all()
    context = {'list':qs}
    
    return render(request,'students/list.html',context)

    # text='''
    #     <html>
    #         <head></head>
    #         <body>
    #             <h2>학생리스트 페이지</h2>
    #         </body>
    #     </html>
    #     '''

    # return HttpResponse('txt')
    
# 학생등록 페이지    
def write(request):
    return render(request,'students/write.html')

# 학생등록 저장 페이지    
def write2(request):
    # request.POST[] // 데이터가 없으면 에러, request.POST.get()// 데이터가 없어서 에러안남
    name = request.POST.get('name') 
    major = request.POST.get('major') 
    grade = request.POST.get('grade') 
    age = request.POST.get('age') 
    gender = request.POST.get('gender') 
    print("데이터 정보: ",name,major,grade,age,gender)
    
    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender)
    qs.save()
    
    # 앱 이름으로 찾아가기
    return redirect('students:list')    # app 이름을 찾아서 list로 이동
    # return redirect('/students/list')    # url 주소로도 가능
    # return HttpResponseRedirect(reverse('students:list'))
    # return render(request,'students/write.html')