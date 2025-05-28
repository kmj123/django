from django.shortcuts import render

def send(request,name,age):
    print("전달받은 값: ", name,age)
    context = {"name":name,"age":age}
    return render(request,'students/send.html',context)

def write(request):
    return render(request,'students/write.html')

def result(request):
    name = request.POST.get("name")
    kor = request.POST.get("kor")
    eng = request.POST.get("eng")
    total = int(kor)+int(eng)   # 타입변경 -> 합계 계산
    hobbys = request.POST.getlist("hobby")
    print("입력된 name: ", name)
    print("입력된 kor: ", kor)
    print("입력된 eng: ", eng)
    print("입력된 hobbys: ", hobbys)
    
    context = {"name":name,"kor":kor,"eng":eng,"hobby":hobbys,"total":total}
    return render(request,"students/result.html",context)

def view(request):
    # get방식
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름: ",name)
    print("나이: ",age)
    context = {"name":name,"age":age}
    return render(request,'students/view.html',context)


def list(request):
    # Request -> id=aaa, pw=1111
    id = request.POST.get("id")     # 변수
    pw = request.POST.get("pw")     # 변수
    gender = request.POST.get("gender") # 변수
    hobbys = request.POST.getlist("hobby")  # 리스트
    print("입력된 id: ",id)
    print("입력된 pw: ",pw)
    print("입력된 gender: ",gender)
    print("입력된 hobbys: ",hobbys)
    context = {"id":id, "pw":pw, "gender":gender, "hobby":hobbys}   # 변수명: 객체
    return render(request,'students/list.html',context)