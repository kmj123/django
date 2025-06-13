from django.shortcuts import render,redirect
from board.models import Board
from comment.models import Comment

# 게시판 뷰페이지
def view(request,bno):
    ## db에서 가져오기
    # filter 리스트로 get 한 개만
    ## filter로 찾아오는 경우 array 가져와야함 qs[0]
    qs = Board.objects.get(bno=bno)
    # 댓글 3개 입력
    c_qs = Comment.objects.filter(board=qs).order_by('-cno') 
    
    context = {'board':qs,'c_list':c_qs}
    return render(request,'board/view.html',context)

# 게시판 리스트
def list(request):
    ## db에서 가져오기
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list.html',context)
