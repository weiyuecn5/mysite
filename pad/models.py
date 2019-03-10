from django.db import models

class shujuku(models.Model):
    账号编号=models.CharField(max_length=100,primary_key=True)
    石头数量=models.CharField(max_length=100,blank=True)
    等级=models.CharField(max_length=100,blank=True)
    更新时间=models.CharField(max_length=100,blank=True)
    宠物=models.TextField()
class duizhao(models.Model):
    宠物编号=models.CharField(max_length=100,primary_key=True)
    宠物名字=models.CharField(max_length=100,blank=True)
    宠物价值 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.账号编号
