from django.shortcuts import HttpResponse
from django.core import serializers
from django.views import View
from api.models import Book

# Create your views here.

#FBV
# def index(request):
#     if request.method == "GET":
#         return HttpResponse("GET")
#     elif request.method == "POST":
#         return HttpResponse("POST")
#     elif request.method == "DELETE":
#         return HttpResponse("DELETE")


#CBV

class IndexView(View):
    def get(self, request):
        return HttpResponse("CBV GET")

    def post(self, request):
        return HttpResponse("CBV POST")

    def delete(self, request):
        return HttpResponse("CBV delete")

class BookView(View):

    def get(self, request):
        book_list = Book.objects.all()

        # 序列化：
        data_json = serializers.serialize("json", book_list)

        return HttpResponse(data_json, content_type="json")