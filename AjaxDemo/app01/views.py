from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import User

import json
def index(request):
    print("index")
    return HttpResponse("<h1>hello middle ware test</h1>")


def reg(request):
    return render(request, "reg.html")
# Create your views here.

def username_auth(request):
    print(request.POST)
    #获取客户端数据
    username = request.POST.get("username")

    #校验用户名是否存在
    res = {"exist": False,"msg":""}
    ret = User.objects.filter(name=username)
    if ret:
        #用户名存在
        res["exist"] = True
        res["msg"] = "Username Exist"

    # return HttpResponse(json.dumps(res))
    return JsonResponse(res)

def add(request):
    print(request.POST)
    num1 = request.POST.get("n1",0)
    num2 = request.POST.get("n2",0)
    return HttpResponse(str(int(num1)+int(num2)))

def timer(request):
    return HttpResponse("<h3>Time now 2012-12-12</h3>")