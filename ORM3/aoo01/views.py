from django.shortcuts import render, HttpResponse
from .models import Publish, Author, Book
# Create your views here.

def test(request):
    # publish_list = Publish.objects.all()
    # #1 slice
    # print(publish_list[0])
    # print(publish_list[0:2])
    # #2 iterate
    # for i in publish_list:
    #     print(i.name, i.email)
    # #3 惰性查询
    # queryset = Publish.oobjects.all() #使用的时候才执行
    # for publish in queryset:
    #     print(publish)

    #4 cache机制: 只有遍历了的queryset才会缓存
    queryset = Publish.oobjects.all()

    print(queryset) # hits database
    print(queryset) # hits database
    print(queryset) # hits database

    ret = [publish for publish in queryset] #hits database
    print(queryset) # use cache

    #5 exists 和 iterator
    # Publish 是否有记录
    ret = Publish.objects.all()
    if ret.exists(): # 等价于limit 1
        print("存在出版社")
    else:
        print("不存在")

    # 防止Cashe生产，避免把数据都压入内存而是放入迭代器中
    iterator = Publish.objects.all().iterator()
    for i in iterator:
        print(i)

    for i in iterator:   # 迭代器在第一次已经迭代到底了，也就是一次性的。
        print(i)


    return HttpResponse('ok')