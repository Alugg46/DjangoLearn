from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    # verifier if login or not
    # is_login = request.COOKIES.get("is_login")
    is_login = request.get_signed_cookie("is_login", salt="123456")
    if is_login == "true":
        # user_id = request.COOKIES.get("user_id")
        user_id = request.get_signed_cookie("user_id", salt="123456")
        username = User.objects.get(pk=user_id).name
        return render(request, "cookie/index.html", {"username": username})
    else:
        return redirect(login)

def login(request):
    if request.method == "GET":
        return render(request, "cookie/login.html")
    else:
        user = request.POST.get("user")
        pwd= request.POST.get("pwd")
        try:
            user = User.objects.get(name=user, pwd=pwd)
            res = redirect(index)
            # res.set_cookie("is_login", "true")
            # res.set_cookie("user_id", user.pk, max_age=60)
            res.set_signed_cookie("is_login", "true", salt="123456")
            res.set_signed_cookie("user_id", user.pk, salt="123456")
            return res
        except Exception as e:
            return redirect(login)