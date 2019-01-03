from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import shujuku

for shuju in shujuku.objects.all():
    print(shuju.宠物)