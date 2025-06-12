from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

def blist(request):
    # ajax 전송된 데이터 받기
    id = request.POST.get('id')
    
    # db연결해서 board 모든 데이터를 가져오기
    qs = Board.objects.all().order_by('-bno')   # querySet 
    print('모든 데이터: ',qs)
    
    ### json 타입 변경
    l_qs = list(qs.values())
    print("리스트 타입 데이터:", l_qs)
    
    # ajax로 데이터 전송
    context = {'result':'success','list':l_qs}
    return JsonResponse(context)
