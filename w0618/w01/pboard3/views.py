from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

mlist = []

# 검색기능
### ajax 통신 - 리턴타입 JsonResponse
def searchAjax(request):
    ## 영화데이터 가져오기
    targetDt = request.POST.get('searchInput','20250617')
    print("targetDt: ",targetDt)
    # API 데이터 가져오기
    serviceKey = '3e8375c1bd036b5068d37cbb78fae770'
    # targetDt = '20250617'
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt={targetDt}'
    
    # 공공데이터 가져오기
    response = requests.get(url)
    json_data = json.loads(response.text)   # 타입변경
    
    # 필요한 데이터 가져오기
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    print("10개: ",mlist)
    context ={'list':mlist}
    
    return JsonResponse(context)

# 영화 상세보기
def view(request,movieCd):
    global mlist
    print("mlist",mlist)
    context = {}
    
    for movie in mlist:
        if movie['movieCd'] == str(movieCd):
            context['movieDB'] = movie 
    print("context:",context)
    return render(request,'pboard3/view.html')


# 공공데이터 리스트
def list(request):  
    # 공통영역: 영화데이터 호출
    context = publicScreen('20250617')
    return render(request,'pboard3/list.html',context)

## 공통영역: 영화데이터 가져오기 함수
def publicScreen(targetDt):
    global mlist
    # API 데이터 가져오기
    targetDt = '20250617'
    serviceKey = '3e8375c1bd036b5068d37cbb78fae770'
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt={targetDt}'
    
    response = requests.get(url)
    # 타입변경
    json_data = json.loads(response.text)
    
    # 필요한 데이터 가져오기
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']  # 부모태그 가져오기
    print(mlist)
    context ={'list':mlist}
    
    return context
