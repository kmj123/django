from django.urls import path,include
from . import views 

app_name='students'
urlpatterns = [
    path('list/', views.list,name='list'),  # 전체페이지
    path('write/', views.write,name='write'),   # 등록화면
    path('writeOk/', views.writeOk,name='writeOk'), # 등록하기
    path('view/<str:name>/', views.view,name='view'),  # 상세정보
]
