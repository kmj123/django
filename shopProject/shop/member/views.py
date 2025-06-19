from django.shortcuts import render,redirect
from member.models import Member
from django.http import JsonResponse
import random
import numpy as np

### 전역변수
random_txt = ''

def step03(request):
    return render(request,'member/step03.html')

def step02(request):
    if c_chk != 1:
        return redirect('/')
    else:
        return render(request,'member/step02.html')

# 회원가입 01
def step01(request):
    return render(request,'member/step01.html')

# 이메일 발송
def emailSend(request):
    email = request.POST.get('email')
    print('넘어온 이메일 주소: ',email)

    ### 이메일 발송부분 추가
    
    ####################    
    context={'msg':'success','random_txt':randomNumber()}
    return JsonResponse(context)

# 랜덤번호
def randomNumber():
    # 알파벳 26개, 숫자 10개 : 36개  0-35
    txt = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_array = [] # 초기화
    random_array = np.random.randint(0, 35, 10)
    global random_txt
    for i in random_array:
         random_txt += txt[i]
    
    return random_txt

# 이메일 발송
def confirmChk(request):
    global c_chk
    confirmTxt = request.POST.get('confirmTxt')
    if random_txt == confirmTxt:
        msg = 'success'
        c_chk = 1
    else: 
        msg = 'fail'
        
    context = {'msg':'success'}
    return JsonResponse(context)


# 로그아웃
def logout(request):
    # 세션 모두 삭제
    request.session.clear()
    msg = 2
    msg = 0
    context = {'msg':msg}
    return render(request,'member/login.html',context)

    
# get: 로그인페이지, post: 로그인 확인
def login(request):
    ## 쿠키 정보 가져오기
    cook_id  = request.COOKIES.get('cook_id','')
    context= {'cook_id':cook_id}
    
    if request.method == 'GET':
        return render(request,'member/login.html',context)
    elif request.method == 'POST':        
        # 데이터 POST방식으로 가져오기
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print("넘어온 id,pw,idsave: ",id,pw,idsave)
        
        ## DB확인
        qs = Member.objects.filter(id=id,pw=pw)     #   None - None !=/ ==
        # qs = Member.objects.get(id=id,pw=pw)      #   error - try:except
        if qs:  # 로그인 가능
            msg = 1
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
        else:   # 로그인 불가
            msg = 0
        
        context['msg'] = msg
        response = render(request,'member/login.html',context)
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24) # 하루동안 쿠키 저장
        else:
            response.delete_cookie('cook_id')
            
        return response