from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),     # 아무것도 들어오지 않으면 home home app > urls.py
    path('students/', include('students.urls')),    # students app > urls.py 로 연결 : http://127.0.0.1:8000/students/
    path('event/', include('event.urls')),   
    path('stuscore/', include('stuscore.urls')),   
]
