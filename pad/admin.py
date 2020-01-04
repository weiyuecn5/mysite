from django.contrib import admin
from .models import *

class ShujukuAdmin(admin.ModelAdmin):
    list_display = ('账号编号','石头数量','更新时间','已卖')
    ordering = ('账号编号',)
class DuizhaoAdmin(admin.ModelAdmin):
    list_display = ('宠物编号','宠物名字','宠物价值')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','created_time','modified_time')
    ordering = ('-created_time',)
class HotAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(shujuku,ShujukuAdmin)
admin.site.register(duizhao,DuizhaoAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Hot,HotAdmin)