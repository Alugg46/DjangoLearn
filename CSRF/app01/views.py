from django.shortcuts import render, HttpResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html", locals())
    else:
        user = request.POST.get("user", 0)
        pwd = request.POST.get("pwd", 0)
        print(user, pwd)
        res = {"state": False, "msg":"错误"}
        if user== "yuan" and pwd== "123":
            res["state"] = True
            res["msg"] = None
        return JsonResponse(res)


def get_tokens(request):
    token = get_token(request)
    return HttpResponse(token)


def index(request):
    return HttpResponse("This is index")