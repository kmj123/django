from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from.import views


app_name ='customer'
urlpatterns = [
    path('list/', views.list,name='list'),
    path('view/<int:bno>/', views.view,name='view'),
    path('write/', views.write,name='write'),
    path('delete/<int:bno>/', views.delete,name='delete'),
    path('update/<int:bno>/', views.update,name='update'),
]
