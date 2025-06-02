from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('notice_list/', views.notice_list,name='notice_list'),
    path('notice_read/', views.notice_read,name='notice_read'),
    path('write/', views.write,name='write'),
]
