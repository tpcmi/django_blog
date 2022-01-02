from typing import Text
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # ForeignKey：第一个参数指向引用的模型，第二个参数指向当外键引用模型数据被删除时兜底的操作，
    #             如此处cascade是指，主键更新，外键表也跟着更新，主键删除，外键表该行也删除
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save
    
    def __str__(self):
        return self.title



