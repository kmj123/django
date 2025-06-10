from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers # json 타입 생성
from django.views.decorators.csrf import csrf_exempt

def list(request):
    return HttpResponse('데이터 전달')