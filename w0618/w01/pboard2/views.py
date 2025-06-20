from django.shortcuts import render
import requests
import json

### 전역변수
dlist = []  # list함수에서 공공데이터를 가지고와서 view함수에 전달

# 공공데이터 상세보기
def view(request,galContentId):
    global dlist
    print('넘어온 galContentId: ',galContentId)
    print(dlist)
    context = {}
    for d in dlist:
        if d['galContentId'] == str(galContentId):
            context['dData'] = d
    
    print(context['dData'])
    return render(request,'pboard2/view.html',context)

# 공공데이터 리스트
def list(request):
    global dlist # 전역변수 사용 
    ## 공공데이터 가져오기에 필요한 정보
    pageNo = 1
    serviceKey = 'bFRK9ZqnlUcL84dUtWGKOmdZnXef3GjD0E%2Fj%2BBUl6YM4BHktIhTmnpHvI6RjRvy9Ew25Nb0SDVMGQOldDDgQiA%3D%3D'
    ### url https 's' 꼭 빼주기@@
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={serviceKey}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    
    # 공공데이터 가져오기
    response = requests.get(url)             # 공공데이터 기본 타입: str 타입
    print("공공데이터: ",response.text)
    json_data = json.loads(response.text)    # json 타입으로 변경 : dict 타입 []
    # 필요한 데이터 리스트로 변경해서 전달
    dlist = json_data['response']['body']['items']['item']  # dlist에 10개 데이터가 들어감
    print("10개: ", dlist)
   
    context = {'list':dlist}
    return render(request,'pboard2/list.html',context)
