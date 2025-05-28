from django.urls import path, include
from.import views

app_name = 'event'   # students app > urls.py 로 연결 : http://127.0.0.1:8000/event/list/
urlpatterns = [
    path('event/', views.event, name='event'),   # list url -> list 함수 호출
]
