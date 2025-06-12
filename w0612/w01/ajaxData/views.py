from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

# 게시글삭제
def bdelete(request):
    bno = request.POST.get(bno)
    ## db 삭제
    qs = Board.objects.get(bno=bno)
    qs.delete()
    context = {'result':'success'}
    return JsonResponse(context)

def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    
    ## db 저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    ## json 타입으로 변환
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    
    context={'result':'success','board':l_qs}
    return JsonResponse(context)

# form 게시판 - get,post
def blist(request):
    ### db 게시글 전체 가져오기
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print('queryset 데이터: ', qs)
    
    ### json 타입으로 변경
    l_qs = list(qs.values())
    print('리스트 타입:' , l_qs)
    
    
    context={'result':'success','list':l_qs}
    return JsonResponse(context)
    