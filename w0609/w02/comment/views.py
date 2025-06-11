from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers # json 타입 생성
from django.views.decorators.csrf import csrf_exempt    # csrf 토큰이 없을때 예외 처리
from member.models import Member
from board.models import Board
from comment.models import Comment

# 하단댓글 삭제
def cdelete(request):
    # cno 데이터 확인
    cno = request.POST.get('cno')
    print('하단댓글 번호: ', cno)
    qs = Comment.objects.delete(cno=cno)
    qs.delete()
    context = {'result':'success'}
    return JsonResponse(context)

# 하단댓글 저장
def cwrite(request):
    id = request.session['session_id']  # 로그인이 되어야 하단댓글 가능
    # id = 'aaa'
    member = Member.objects.get(id=id)
    bno = request.POST.get('bno',1)
    board = Board.objects.get(bno=bno)
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent','')
    print("넘어온데이터: ",cpw,ccontent)
    # QuerySet 타입 -> list 타입
    qs = Comment.objects.create(board=board,member=member,cpw=cpw,
                                ccontent=ccontent)
    
    # print('qs: ',qs)    # ok
    
    # filter 리스트 타입으로 리턴
    list_qs = list(Comment.objects.filter(cno=qs.cno).values())  
    print('list_qs: ', list_qs)
    context= {'result':'success','comment':list_qs}
    
    return JsonResponse(context)
