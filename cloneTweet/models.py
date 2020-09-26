from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id = models.AutoField(primary_key=True) <- 자동으로 생성됨
    content = models.TextField(blank=True, null=True)
    img = models.FileField(upload_to="image/", blank=True, null=True)
