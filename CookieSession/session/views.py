import datetime

from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    # read session
    #1. get key of session_id
    #2. select key in Django_session
    #3. get session-data.get("user_id")
    user_id = request.session.get("user_id")

    if user_id:
        # alread logined
        user = User.objects.get(pk=user_id)
        return render(request, "session/index.html", {"username": user.name})
    else:
        return redirect("/session/login")

def login(request):
    if request.method == "GET":
        return render(request, "session/login.html")
    else:
        user = request.POST.get("user")
        pwd= request.POST.get("pwd")
        try:
            user = User.objects.get(name=user, pwd=pwd)
            # Write session
            #1.create a random string
            #2.random stirng as seesion key, insert key and value of session as session value into Django_seesion
            #3.return a cookie contains session_id and random string to client
            request.session["user_id"] = user.pk
            # return redirect(index)
            return redirect(index)

        except Exception as e:
            return redirect("/session/login")

def logout(request):
    # 删除整条cookie
    # request.session.flush()

    # 删指定的键值对cookie
    del request.session["user_id"]
    return redirect("/session/login")


def shop(request):
    # 取上一次访问时间
    last_visit_time = request.session.get("last_visit_time", "第一次登录")

    #Save current time as
    now = datetime.datetime.now().strftime("%Y/%m/%d %X")
    request.session["last_visit_time"] = now

    return render(request,"session/shop.html", {"last_visit_time": last_visit_time})

