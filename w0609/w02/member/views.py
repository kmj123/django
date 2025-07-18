from django.shortcuts import render,redirect
from member.models import Member

# 로그아웃 구현
def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)

# 로그인 부분   - get, post
def login(request):
    if request.method == 'GET': # 로그인페이지로 이동
        ## 쿠키 읽어오기
        cook_id = request.COOKIES.get('cook_id','')
        context = {'cook_id':cook_id}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':  # 로그인 구현
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print("로그인 넘어온 데이터: ",id,pw,idsave)
        
        # 가져온 데이터를 Member테이블의 데이터와 비교하기
        # filter - 리스트타입으로 get - 한개만
        ## id, pw 확인
        msg = 0
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = id  # session id를 추가
            request.session['session_name'] = qs.name  # session name을 추가
            msg = 1
        except: print('데이터가 없습니다')
        ## 쿠키 읽어오기
        cook_id = request.COOKIES.get('cook_id','')
        context = {'msg':msg,'cook_id':cook_id}
        response = render(request,'member/login.html',context)
        ## 쿠키저장
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24*30)    # id를 쿠키 저장
        else:
            response.delete_cookie('cook_id')    # idsave 쿠키 삭제
        return response


# 회원가입 완료 부분
def step04(request,name):
    print("name: ",name)
    context = {'name':name}
    return render(request,'member/step04.html',context)


# 회원가입 부분
def step03(request):
    if request.method == 'GET':
        return render(request,'member/step03.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email = f'{email1} @ {email2}'
        emailc = request.POST.get('emailc')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        phone3 = request.POST.get('phone3')
        phone = f'{phone1}-{phone2}-{phone3}'
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        birth1 = request.POST.get('birth1')
        birth2= request.POST.get('birth2')
        birth3= request.POST.get('birth3')
        birth= f'{birth1}-{birth2}-{birth3}'
        corporate = request.POST.get('corporate')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ','.join(hobbys)
        print("넘어온데이터: ",name,id,email1,email2,email,emailc,address1,address2,phone,tel,birth,corporate,gender,hobby)
        
        ### Member 테이블 저장
        Member.objects.create(name=name,id=id,email=email,emailc=emailc,
                              address1=address1,address2=address2,phone=phone,
                              tel=tel,birth=birth,corporate=corporate,
                              gender=gender,hobby=hobby)
        
        
        return redirect(f'/member/step04/{name}/')

# 약관동의
def step02(request):
    return render(request,'member/step02.html')


# 이메일 인증 부분
def step01(request):
    return render(request,'member/step01.html')