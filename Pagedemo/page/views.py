from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Book
from django.core.paginator import Paginator, EmptyPage


def create_multi(request):
    book_list = []
    for i in range(1, 1001):
        book = Book(title="Book"+str(i), price=i *2)
        book_list.append(book)
    Book.objects.bulk_create(book_list)
    return HttpResponse(" Insert sucess")

def books(request):
    book_list = Book.objects.all()
    #(1) 分页对象
    paginator = Paginator(book_list, 100) #每页100条
    # #分页情况
    # print(paginator.count)  #数据量
    # print(paginator.num_pages) #分页数
    # print(paginator.page_range) #分页列表
    #
    # #(2)获取某页对象
    # page02 = paginator.page(2)
    # #获取该页所有数据
    # #方式1
    # print(page02.object_list)
    # #方式2
    # for book in page02:
    #     print(book)
    #
    # #其他属性
    # print(page02.next_page_number())
    # print(page02.previous_page_number())
    # print(page02.has_next())
    # print(page02.has_previous())

    #获取某页数据
    try:
        visit_page_num = int(request.GET.get("page"))
        page = paginator.page(visit_page_num)
        if visit_page_num == 1:
            page_range = range(1,4)
        elif visit_page_num == paginator.num_pages:
            page_range = range(paginator.num_pages-2, paginator.num_pages +1)
        else:
            page_range = [visit_page_num-1, visit_page_num, visit_page_num+1]
    except EmptyPage:
        page = paginator.page(1)

    # return render(request, "index.html", {"page": page, "paginator": paginator, "visit_page_num": visit_page_num})
    return render(request, "index2.html", {"page": page, "paginator": paginator, "page_range": page_range,"visit_page_num":visit_page_num})