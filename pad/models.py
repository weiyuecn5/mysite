from django.db import models

class shujuku(models.Model):
    账号编号=models.CharField(max_length=100,primary_key=True)
    石头数量=models.CharField(max_length=100,blank=True)
    等级=models.CharField(max_length=100,blank=True)
    更新时间=models.CharField(max_length=100,blank=True)
    宠物=models.TextField()
    已卖=models.CharField(max_length=20,default='0')
    买家=models.CharField(max_length=100,blank=True)
    价格=models.CharField(max_length=100,blank=True)
class duizhao(models.Model):
    宠物编号=models.CharField(max_length=100,primary_key=True)
    宠物名字=models.CharField(max_length=100,blank=True)
    宠物价值 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.账号编号
class huancun(models.Model):
    #缓存数据库 存放新加入的数据
    #唯一键=账号编号-石头数量-宠物-时间
    唯一键=models.CharField(max_length=150,primary_key=True)
    账号编号=models.CharField(max_length=100)
    石头数量=models.CharField(max_length=100,blank=True)
    等级=models.CharField(max_length=100,blank=True)
    宠物=models.TextField()
    是否上传=models.CharField(max_length=2,default='1')
    更新时间=models.CharField(max_length=100,blank=True)