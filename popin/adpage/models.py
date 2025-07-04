from django.db import models
from django.db import models

class Notice(models.Model):
    NOTICE_TYPES = [
        ('일반', '일반'),
        ('업데이트', '업데이트'),
        ('점검', '점검'),
    ]

    title = models.CharField("제목", max_length=200)
    content = models.TextField("내용")
    notice_type = models.CharField("공지 유형", max_length=20, choices=NOTICE_TYPES, default="일반")
    is_pinned = models.BooleanField("상단 고정", default=False)

    file = models.FileField("첨부파일", upload_to="notice_files/", blank=True, null=True)

    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    views = models.PositiveIntegerField("조회수", default=0)

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return f"[{self.notice_type}] {self.title}"