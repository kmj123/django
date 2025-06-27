from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'signup'
urlpatterns = [
    path('agree/', views.agree, name='agree'),
    path('signup/', views.signup, name='signup'),
    path('location_select/', views.location_select, name='location_select'),
    path('member_select/', views.member_select, name='member_select'),
    path('completed/', views.completed, name='completed'),
    
]
