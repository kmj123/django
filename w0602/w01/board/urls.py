from django.urls import path,include
from. import views

app_name='board'
urlpatterns = [
    path('', views.list, name='list'),     # 게시판 리스트 페이지
    path('list/', views.list, name='list'),     # 게시판 리스트 페이지
    path('write/', views.write, name='write'),  # 글쓰기 페이지
    path('view/<int:bno>/', views.view, name='view'),     # 글 상세페이지
    path('update/<int:bno>/', views.update, name='update'),   # 글 수정
]
