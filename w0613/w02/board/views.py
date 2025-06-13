from django.shortcuts import render,redirect
from board.models import Board
from comment.models import Comment

# 게시판 리스트
def list(request):
    return render(request,'board/list.html')
