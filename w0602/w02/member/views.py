from django.shortcuts import render

def login(request):
    if request.method == "GET":
        print("모든 쿠키",request.COOKIES)
        idSave = request.COOKIES.get('idSave','')   # 아이디를 가져오고 없으면 공백
        context = {""}
        return render(request,'member/login.html')
    
    elif request.method == "POST":
        return

def join01(request):
    return render(request,'member/join01.html')

def join02(request):
    return render(request,'member/join02.html')

def join03(request):
    return render(request,'member/join03.html')

def modifying_member_info(request):
    return render(request,'member/modifying_member_info.html')
