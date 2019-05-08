from django.shortcuts import render
import time
from django.http import HttpResponse
from .models import *

def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    else:
        bh_1=request.POST.get('bh_1')
        bh_2=request.POST.get('bh_2')
        bh_3=request.POST.get('bh_3')
        bh_4=request.POST.get('bh_4')
        bh_5=request.POST.get('bh_5')
        if bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        else:
            return render(request, 'index.html')

def wy(request):
    if request.method=='GET':
        return render(request, 'wy.html')
    else:
        bh_1=request.POST.get('bh_1')
        bh_2=request.POST.get('bh_2')
        bh_3=request.POST.get('bh_3')
        bh_4=request.POST.get('bh_4')
        bh_5=request.POST.get('bh_5')
        zhbh = request.POST.get('zhbh')
        if zhbh:
            shujus = shujuku.objects.filter(账号编号__icontains=zhbh)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        elif bh_1:
            shujus=shujuku.objects.filter(宠物__icontains=bh_1)
            for shuju in shujus:
                shuju.宠物=chuli(shuju.宠物)
            return render(request, 'jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
        else:
            return render(request, 'wy.html')

def addshuju(request):
    if request.method == 'GET':
        return render(request,'addshuju.html')
    else:
        zhbh=request.POST.get("zhbh") #账号编号
        stsl=request.POST.get("stsl") #石头数量
        zhdj=request.POST.get("zhdj") #账号等级
        cwbh=request.POST.get("cwbh") #宠物编号
        cwmz=request.POST.get("cwmz") #宠物名字
        cwjz=request.POST.get("cwjz") #宠物名字
        gxsj=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) #更新时间
        try:
            if zhbh:
                shuju=shujuku.objects.get(账号编号=zhbh)
                shuju.宠物=shuju.宠物+cwbh+','
                if stsl:
                    shuju.石头数量=stsl
                if zhdj:
                    shuju.等级 = zhdj
                shuju.更新时间=gxsj
                shuju.save()
                return HttpResponse('账号:%s 已更新!'%zhbh)
            if cwbh and cwmz:
                shuju_id=duizhao(宠物编号=cwbh,宠物名字=cwmz,宠物价值=cwjz)
                shuju_id.save()
                return HttpResponse('%s-%s-%s'%(cwbh,cwmz,cwjz))
        except:
            shuju=shujuku(账号编号=zhbh,石头数量=stsl,等级=zhdj,更新时间=gxsj,宠物=cwbh+',')
            shuju.save()
            return HttpResponse('账号:%s 已更新!' % zhbh)
def delshuju(request,zhid):
    try:
        shuju=shujuku.objects.get(pk=zhid)
        shuju.delete()
        return HttpResponse('编号:%s 已经删除!'%zhid)
    except:
        return HttpResponse('编号:%s 不存在!'%zhid)

def add(request,wyid,zhid,st='0',dj='0',cw='0'): #/唯一键/账号编号/石头数量/等级/宠物编号/
    gxsj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 更新时间
    shuju=huancun(唯一键=wyid,账号编号=zhid,石头数量=st,等级=dj,宠物=cw,更新时间=gxsj)
    shuju.save()
    return HttpResponse(wyid)

def upshuju(request):
    newdatas=huancun.objects.filter(是否上传='1')
    for newdata in newdatas:
        try:
            shuju=shujuku.objects.get(账号编号=newdata.账号编号)
            shuju.石头数量=newdata.石头数量
            shuju.等级=newdata.等级
            shuju.更新时间=newdata.更新时间
            shuju.宠物=shuju.宠物+newdata.宠物+','
            shuju.save()
            newdata.是否上传='0'
            newdata.save()
        except:
            shuju=shujuku(账号编号=newdata.账号编号,石头数量=newdata.石头数量,等级=newdata.等级,更新时间=newdata.更新时间,宠物=newdata.宠物+',')
            shuju.save()
            newdata.是否上传='0'
            newdata.save()
    return HttpResponse('更新')

def chuli(cw):
    cw_1 = '\n75000宠物:\n'
    cw_2 = '50000宠物:\n'
    cw_3 = '6000宠物:\n'
    cw_4 = '15000宠物:\n'
    cw_6 = '25000宠物:\n'
    cw_5 = '其他宠物:\n'
    for data in cw.split(','):
        if len(data) > 4 or len(data) < 3:
            continue
        else:
            try:
                a = duizhao.objects.get(pk=data)
                if int(a.宠物价值)==75000:
                    cw_1=cw_1+'[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值)==50000:
                    cw_2 = cw_2 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值) == 25000:
                    cw_6 = cw_6 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值) == 15000:
                    cw_4 = cw_4 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值)==6000:
                    cw_3 = cw_3 + '[' + a.宠物编号 + a.宠物名字 + '] '
                else:
                    cw_5 = cw_5+ '[' + a.宠物编号 + a.宠物名字 + '] '
            except:
                pass
    return cw_1+'\n'+cw_2+'\n'+cw_6+'\n'+cw_4+'\n'+cw_3+'\n'+cw_5

def chuli_1(cw):
    cw_1 = '\n'
    for data in cw.split(','):
        if len(data) > 4 or len(data) < 3:
            continue
        else:
            try:
                a = duizhao.objects.get(pk=data)
                cw_1=cw_1+'[' + a.宠物编号 + a.宠物名字 + '] '
            except:
                pass
    return cw_1+'\n'