from django.urls import path, include
from.import views

app_name = 'stuscore'   # stuscore app > urls.py 로 연결 : http://127.0.0.1:8000/stuscore/list/
urlpatterns = [
    path('list/', views.score, name='list/'),   # list url -> list 함수 호출
]

