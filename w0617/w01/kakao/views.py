from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def oauth(request):
    code = request.GET.get('code')
    print("CODE: ",code)
    return HttpResponse()