from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import *

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        tj_1 = request.POST.get("tj_1")
        tj_2 = request.POST.get("tj_2")
        tj_3 = request.POST.get("tj_3")
        tj_4 = request.POST.get("tj_4")

        try:
            cxjg = []
            if tj_4:
                cxjg.append(get_data(tj_4))
                # print(cxjg)
                return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
            elif tj_1 and tj_2 and tj_3:
                for cw in shujuku.objects.all():
                    if tj_1 in cw.宠物 and tj_2 in cw.宠物 and tj_3 in cw.宠物:
                        cxjg.append(get_data(cw.账号编号))
                if len(cxjg)>0:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
                else:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
            elif tj_1 and tj_2:
                for cw in shujuku.objects.all():
                    if tj_1 in cw.宠物 and tj_2 in cw.宠物:
                        cxjg.append(get_data(cw.账号编号))
                if len(cxjg)>0:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
                else:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
            elif tj_1:
                for cw in shujuku.objects.all():
                    if tj_1 in cw.宠物:
                        cxjg.append(get_data(cw.账号编号))
                if len(cxjg)>0:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
                else:
                    return render(request, 'jg.html', {'shuju': cxjg,'shuliang':len(cxjg)})
        except:
                return render(request,'jg.html',{'shuliang':0})
        return  render(request,'jg.html',{'shuliang':0})

def addshuju(request):
    if request.method == 'GET':
        return render(request,'addshuju.html')
    else:
        zhbh=request.POST.get("zhbh") #账号编号
        stsl=request.POST.get("stsl") #石头数量
        zhdj=request.POST.get("zhdj") #账号等级
        cwbh=request.POST.get("cwbh") #宠物编号
        cwmz=request.POST.get("cwmz") #宠物名字
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
                shuju_id=duizhao(宠物编号=cwbh,宠物名字=cwmz)
                shuju_id.save()
                return HttpResponse('%s:%s'%(cwbh,cwmz))
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

def add(request,zhid,st='0',dj='0',cw='0'): #/账号编号/石头数量/等级/宠物编号/
    gxsj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 更新时间
    try:
        shuju=shujuku.objects.get(账号编号=zhid)
        if st != '0':
            shuju.石头数量 = st
        if dj != '0':
            shuju.等级 = dj
        if cw != '0':
            shuju.宠物 = shuju.宠物 + cw + ','
        shuju.更新时间 = gxsj
        shuju.save()
        return HttpResponse('账号:%s 已更新!' % zhid)
    except:
        shuju = shujuku(账号编号=zhid, 石头数量=st, 等级=dj, 更新时间=gxsj, 宠物=cw+',')
        shuju.save()
        return HttpResponse('账号:%s 已更新!' % zhid)


def get_data(a):
    all_cw='' #所有处理过的宠物数据
    li=[]
    shuju = shujuku.objects.get(账号编号=a)
    for data in shuju.宠物.split(','):
        if len(data) > 4 or len(data) < 3:
            continue
        else:
            try:
                a = duizhao.objects.get(pk=data)
                all_cw = all_cw + '[' + a.宠物编号 + a.宠物名字 + '] '
                shuju.宠物 = all_cw
            except:
                pass
    li.append(shuju.账号编号)
    li.append(shuju.石头数量)
    li.append(shuju.等级)
    li.append(shuju.更新时间)
    li.append(shuju.宠物)
    return li