from django.shortcuts import render

def notice_list(request):
    return render(request,'board/notice_list.html')

def notice_read(request):
    return render(request,'board/notice_read.html')

def write(request):
    return render(request,'board/write.html')


