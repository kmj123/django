from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from.import views


app_name ='comment'
urlpatterns = [
    path('clist/', views.clist,name='clist'),
    path('cdelete/', views.cdelete,name='cdelete'),
]
