from django.shortcuts import render
import requests
import json

# 전역변수 선언
global list

# 공공데이터 상세보기
def view(request,galContentId):
    print("넘어온 galContentId: ", galContentId)
    ## 공공데이터 호출
    dlist = publicData()

    for d in dlist:
        print("데이터1 : ",d['galContentId'])
        # AttributeError: 'dict' object has no attribute 'galContentId'
        if d['galContentId'] == str(galContentId):  ## 타입확인해서 타입변환
            print('검색된 데이터: ',d)
            dData = d
            break
        
    context = {'dData':dData}
    return render(request,'pboard/view.html',context)

# 공공데이터 함수 호출
def list(request):
    dlist = publicData()
    context = {'list':dlist}
    return render(request,'pboard/list.html',context)
 
# 공공데이터 가져오기 함수   
def publicData():
    # 인증키
    public_key = '918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    pageNo = 1
    # api 주소
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래핑 requests
    response = requests.get(url)
    # print("공공데이터 : ",response.text)  # str타입
    
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    dlist = json_data['response']['body']['items']['item']
    # print('json데이터 : ',json_data['response']['body']['items']['item'])     # json타입
    # print('json데이터 1개 : ',json_data['response']['body']['items']['item'][0])
    
    return dlist