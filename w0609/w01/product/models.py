from django.db import models

# 상품관리 DB 설계
# 상품코드 숫자
# 상품명 문자
# 상위 카테고리 문자
# 하위 카테고리 문자
# 원산지 문자
# 중량 숫자
# 소비자 가격 숫자
# 할인가 숫자
# 재고 숫자
# 메인 이미지 이미지
# 서브 이미지1 이미지
# 서브 이미지2 이미지
# 등록일자 날짜
# 수정일자 날짜
# 판매여부 문자
# 상위노출 숫자(역순정렬, 순차정렬)

class Product(models.Model):
    P_Code = models.IntegerField(default=0,primary_key=True)
    P_MD = models.CharField(max_length=10000)
    Top_MD = models.CharField(max_length=50)
    Low_MD = models.CharField(max_length=50)
    Origin = models.CharField(max_length=50)
    Weight = models.IntegerField(default=0)
    Customer_price = models.IntegerField(default=0)
    Discount_price = models.IntegerField(default=0)
    Stack = models.IntegerField(default=0)
    Main_img = models.ImageField(default=True)
    Sub_img = models.ImageField(default=True)
    Edate = models.DateTimeField(auto_now=True)
    Rdate = models.DateTimeField(auto_now=True)
    Front_top = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.P_MD},{self.Origin},{self.Weight},{self.Customer_price},{self.Discount_price},{self.Stack}'
    
