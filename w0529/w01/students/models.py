from django.db import models


class Student(models.Model):
    # 번호가 순차적으로 증가
    no = models.AutoField(primary_key=True) # sequence 타입
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    hobby = models.CharField(max_length=100,blank=True)
    # 날짜타입
    sdate = models.DateTimeField(auto_now = True)   # date-sysdate
    memo = models.TextField(blank=True) # clob
    
    # 관리자페이지
    # admin에서는 기본적으로 obejct로 객체를 출력하는데 필드를 보고싶을때 사용
    def __str__(self):
        return f"{self.no},{self.name},{self.sdate}"
