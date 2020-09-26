from django.db import models

# Create your models here.
class Tweet(models.Model):
    # class'Tweet' has no 'objects' member 문제가 나타날때 추가
    objects = models.Manager()

    # id = models.AutoField(primary_key=True) <- 자동으로 생성됨
    content = models.TextField(blank=True, null=True)
    img = models.FileField(upload_to="image/", blank=True, null=True)
