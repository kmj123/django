from django.shortcuts import render,redirect   # redirect 임포트
from students.models import Student # 테이블 연결

# 학생정보 삭제
def delete(request,no):
    Student.objects.get(no=no).delete()
    # return redirect('/students/list/')    # url -> name
    return redirect('students:list')    # app_name, path name

# 수정한 학생정보 저장
def updateOk(request):
    no = request.POST.get('no')
    qs = Student.objects.get(no=no) # 데이터 검색
    
    # 데이터 수정
    qs.name = request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    qs.hobby = hobby
    
    qs.save()
    
    return redirect(f'/students/view/{no}/')

# 학생정보 업데이트 페이지 열기
def update(request,no):
    qs = Student.objects.get(no=no) # set타입 1개
    context = {'stu':qs}
    # qs = Student.objects.filter(no=no)  # 데이터타입 - 리스트 타입
    # context = {'stu':qs[0]}
    
    return render(request,'students/update.html',context)

# 학생정보 상세보기
def view(request,no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None
    print("전달 no: ",no)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보 저장 - 저장하기를 눌렀을때 실행할 함수
def writeOk(request):   # if request.method == 'POST':
    # 학생정보 저장
    name = request.POST.get('name')
    major = request.POST['major']
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    memo = request.POST.getlist('memo')
    # 취미 - 리스트
    hobby = request.POST.getlist('hobby')
    # 리스트 타입 -> str타입으로 변경
    hobby = ','.join(hobby)  # game,gofl

    print("저장정보 이름: ",name)
    print("저장정보 학과: ",major)
    print("저장정보 취미: ",hobby)  #['game','golf','swim']
    
    Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo=memo).save()
    
    return redirect('/students/list/')


# 학생정보 등록 - 등록 페이지 열기(학생등록하기를 눌렀을때 가져올 정보)
def write(request):
    if request.method == 'GET':
        return render(request,'students/write.html')

# 학생정보 리스트 - 전체학생 정보를 불러옴
def list(request):
    # Student 테이블 연결
    qs = Student.objects.all()
    context = {'list':qs}
    # render 폴더앞에 / 안붙임
    return render(request,'students/list.html',context)
