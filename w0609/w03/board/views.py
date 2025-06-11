from django.shortcuts import render
# ajax 전송에 필요한 선언
from django.http import JsonResponse

# 4. ajax 데이터 전송방식
def view2(request):
    # html에서 데이터 전달
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # QuerySet, QueryList -> dic 타입이므로 list 타입 변경 필요
    # models DB데이터가 있으면, list 타입으로 변경 후 전송해야함.
    
    # 데이터를 html 전송
    context = {'id':id,'name':name,'result':'success','pw':'1111'}
    # 
    return JsonResponse(context)

# 1. form 데이터 전송 방식 - get,post
def view(request):
    if request.method == 'GET':
        return render(request,'board/view.html')
    
    elif request.method == 'POST':
        # html에서 데이터 전달
        id = request.POST.get('id','')
        name = request.POST.get('name','')

        # 데이터를 html 전송
        context = {'id':id,'name':name}
        print(id,name)
        return render(request,'board/view.html',context)

def list(request):
    return render(request,'board/list.html')