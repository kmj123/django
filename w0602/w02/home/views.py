from django.shortcuts import render

# 로그인페이지 연결, 로그인 확인
def index(request):
    return render(request,'index.html')
