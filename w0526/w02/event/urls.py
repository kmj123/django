from django.urls import path, include
from.import views

app_name=''
urlpatterns = [
    # views.py로 연결
    path('event/',views.event,name='event'),
]
