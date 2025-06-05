from django.shortcuts import render,redirect
from board.models import Board

# 게시글 쓰기
def write(request):
    if request.method =="GET":
        return render(request,'board/write.html')
    elif request.method == "POST":
        # request로 데이터 가져오기
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        # 받아온 데이터 저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg': 1}
        return render(request,'board/write.html',context)

# 게시글 상세보기
def view(request,bno):
    qs = Board.objects.filter(bno=bno)
    context = {'board':qs[0]}
    return render(request,'board/view.html',context)

# 게시글 목록
def list(request):
    qs = Board.objects.all().order_by('-bno')
    context = {'list':qs}
    return render(request,'board/list.html',context)
