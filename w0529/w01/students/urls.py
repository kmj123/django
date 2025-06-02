from django.urls import path,include
from.import views

# app_name = /를 붙이지 않음
app_name='students'
urlpatterns = [
    # path에는 / 를 붙임, name 에는 / 안붙인다.
    path('list/', views.list,name='list'),
    path('write/', views.write,name='write'),
    path('writeOk/', views.writeOk,name='writeOk'),
    # html -> server 1. 파라미터, 2. api 방식 3. js 방법 
    # html/<타입명:변수명>/ <int:no> <str:name>
    path('view/<int:no>/', views.view,name='view'),
    path('update/<int:no>/', views.update,name='update'),   # 학생정보 수정페이지 열기
    path('updateOk/', views.updateOk,name='updateOk'),      # 학생정보 수정 완료
    path('delete/<int:no>', views.delete,name='delete'),    # 학생정보 삭제
]
