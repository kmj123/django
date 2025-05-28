from django.shortcuts import render

def students(request):
    return render(request,'students/list.html')

def write(request):
    return render(request,'students/write.html')

def result(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    print("입력된 id: ",id)
    print("입력된 pw: ",pw)
    print("입력된 gender: ",gender)
    print("입력된 hobbys: ",hobbys)
    context = {"id":id,"pw":pw,"name":name,"gender":gender,"hobby":hobbys}
    return render(request,'students/result.html',context)