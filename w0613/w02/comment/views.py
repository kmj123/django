from django.shortcuts import render,redirect
from django.http import JsonResponse
from comment.models import Comment
from member.models import Member
from board.models import Board

def clist(request):
    context= {'result':'success'}
    return JsonResponse(context)