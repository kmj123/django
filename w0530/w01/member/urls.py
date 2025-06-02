from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('join01_terms/', views.join01_terms,name='join01_terms'),
    path('join02_info_input/', views.join02_info_input,name='join02_info_input'),
    path('join03_success/', views.join03_success,name='join03_success'),
    path('modifying_member_info/', views.modifying_member_info,name='modifying_member_info'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
]



