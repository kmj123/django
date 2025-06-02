from django.shortcuts import render
from member.models import Member

def join01_terms(request):
    return render(request,'member/join01_terms.html')
def join02_info_input(request):
    return render(request,'member/join02_info_input.html')
def join03_success(request):
    return render(request,'member/join03_success.html')
def modifying_member_info(request):
    return render(request,'member/modifying_member_info.html')

## 로그인 구현
def login(request):  # 로그인 화면 이동 
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':  # 로그인확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디, 패스워드:" ,id, pw)
        
        # id가 있는지 확인
        try: 
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                txt = 1 # id가 있음
                print(txt)
        
        except:
            txt = 0 # id가 없음
            print(txt)
            
    return render(request,'member/login.html')
        
    
    
    
