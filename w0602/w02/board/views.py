from django.shortcuts import render
from board.models import Board

# 게시판 리스트
def list(request):
    return render(request,"board/list.html")

# 게시판 글쓰기
def write(request):
    if request.method == "GET":
        print("데이터 없음")
        return render(request,"board/write.html")
    
    elif request.method == "POST":    
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get("bcontent")
        bfile = request.POST.get("bfile")
        
        qs = Board.objects.get(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        
        print("입력한 데이터: ",btitle,bcontent,bfile)
        return render(request,'board/write.html')


