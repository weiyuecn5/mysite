from django.contrib import admin
from .models import shujuku,duizhao
# Register your models here.
class ShujukuAdmin(admin.ModelAdmin):
    list_display = ('账号编号','石头数量','更新时间','已卖')
    ordering = ('账号编号',)
class DuizhaoAdmin(admin.ModelAdmin):
    list_display = ('宠物编号','宠物名字','宠物价值')
    # ordering = ('宠物编号',)


admin.site.register(shujuku,ShujukuAdmin)
admin.site.register(duizhao,DuizhaoAdmin)