from django.urls import path, include
from.import views

app_name = 'students'   # students app > urls.py 로 연결 : http://127.0.0.1:8000/students/list/
urlpatterns = [
    path('list/', views.list, name='list'),   # list url -> list 함수 호출
    path('write/', views.write, name='write'),   # 학생등록 페이지
    path('write2/', views.write2, name='write2'),   # 학생등록 저장 페이지
]
