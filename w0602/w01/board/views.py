from django.shortcuts import render,redirect
from board.models import Board

# 글 수정페이지, 글 수정 저장
def update(request,bno):
    if request.method == "GET":     # 글수정 페이지
        qs = Board.objects.get(bno=bno)
        context ={"board":qs}
        return render(request,'board/update.html',context)  
    elif request.method == "POST":  # 글수정 저장
        # 변경된 게시글 가져오기 - 몇번 게시글 수정이야?
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        # 변경된 게시글 저장
        # 1. 변경할 게시글 가져오기 - 2. 변경된 내용 게시글 저장
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.save()
        
        context = {"msg": 1}    # 글 수정저장 성공
        return render(request,'board/update.html',context)  

# 상세보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'board/view.html',context)

# 쓰기페이지, 쓰기 저장
def write(request):
    if request.method == 'GET':     # 글쓰기 페이지
        return render(request,'board/write.html')
    elif request.method == 'POST':  # 글쓰기 저장
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        # DB 저장 후 qs 변수로 다시 리턴받음
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        print("데이터 확인:", btitle,bcontent,bfile)
        print("데이터 추가:", qs.bgroup, qs.bstep, bfile)
        return redirect('board:list')


# 게시판 리스트 
def list(request):
    # 모든데이터 가져오기
    qs = Board.objects.all().order_by('-bno')
    context = {'list':qs}
    return render(request,'board/list.html',context)
