from django.shortcuts import render
from chart.models import TotalSales
from django.http import JsonResponse

def chlist3(request):
    return render(request,'chart/chlist3.html')

def chlist2(request):
    return render(request, 'chart/chlist2.html')

# ajax으로 json 타입으로 리턴
def chajax(request):
    # db 불러오기 - 하단댓글때 qs list타입으로 변경해서 리턴
    qs = TotalSales.objects.filter(year=2025)
    # print("qs 기본 구문",qs)                           # 타입: QuerySet List 타입
    # print("리스트 타입 구문: ",list(qs.values()))       # 타입: List 타입
    # # json 타입으로 변경
    context ={'ajaxlist':list(qs.values())}
    return JsonResponse(context)

def Schajax(request):
    aYear = request.POST.get('aYear')
    print('넘어온 aYear: ',aYear)
    
    qs = TotalSales.objects.filter(year=aYear)
    context ={'ajaxlist':list(qs.values())}
    return JsonResponse(context)


# 차트페이지 호출
def chlist(request):
    ## DB를 가져와서 차트로 만들기
    # profit = [19,20,21,22,23,24]
    profit = [20,15,7,25,27,30]
    context = {'profit':profit}
    
    # 특정 컬럼 리스트 타입 변경 - 완전한 리스트 형태로 변경 flat=True
    totalSales = TotalSales.objects.filter(year=2025).values_list('totalSales',flat=True)
    print("특정컬럼 리스트:", totalSales)
    
    return render(request,'chart/chlist.html',context)