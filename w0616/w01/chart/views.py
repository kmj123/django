from django.shortcuts import render
from chart.models import TotalSales

# 차트페이지 호출
def chlist(request):
    ## DB를 가져와서 차트로 만들기
    profit = [19,20,21,22,23,24]
    # profit = [20,15,7,25,27,30]
    qs = TotalSales.objects.filter(year=2025)
    print("qs 기본 구문",qs)                           # 타입: QuerySet List 타입
    print("리스트 타입 구문: ",list(qs.values()))       # 타입: List 타입
    print('profit: ',profit)
    
    
    context = {'profit':profit,'list':qs,'list_list':list(qs.values())}
    return render(request,'chart/chlist.html',context)