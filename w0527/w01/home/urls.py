from django.urls import path, include
from.import views

app_name = ''   # students app > urls.py 로 연결 : http://127.0.0.1:8000/students/list/
urlpatterns = [
    path('', views.index, name='index/'),   # list url -> list 함수 호출
]
