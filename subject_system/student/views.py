from django.shortcuts import render, HttpResponse,redirect
from .models import Student, StudentDetail, Clas,Course

# Create your views here.
def index(request):

    student_list = Student.objects.all()
    return render(request, "student/index.html", {"student_list": student_list})

def add_student(request):
    if request.method == "GET":
        class_list = Clas.objects.all()
        return render(request, "student/add_stu.html", {"class_list": class_list})
    else:
        #添加数据到数据库
        #方式1
        name = request.POST.get("user")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        birthday = request.POST.get("birthday")
        clas_id = request.POST.get("clas_id")
        #方式二：前提是模版中 表单名字与字段名 相同
        stu = Student.objects.create(**request.POST.dict())

        return redirect("/student/")


def delete_student(request, del_id):
    student = Student.objects.get(pk=del_id)
    if request.method == "GET":
        return render(request, "student/delete_stu.html", {"student": student})
    else:
        student.delete()
        return redirect("/student/")

def edit_student(request,edit_id):
    student = Student.objects.get(pk=edit_id)
    if request.method =="GET":

        class_list = Clas.objects.all()
        course_list = Course.objects.all()
        return render(request, "student/edit_stu.html", {"edit_stu":student, "class_list": class_list,"course_list":course_list})
    else:
        course_id_list = request.POST.getlist("course_id_list")
        print(course_id_list)
        print(request.POST)
        #获取客户端
        data = request.POST.dict()
        #删除并获取课程id
        data.pop("course_id_list") #多对多的数据要单独处理
        #更新除了多对多以外的数据
        Student.objects.filter(pk=edit_id).update(**data)
        #更新多对多
        student.courses.set(course_id_list)

        return redirect("/student/")

def elective(request):
    course_list = Course.objects.all()
    return render(request, "student/course.html", {"course_list":course_list})

def search(request):
    cate = request.GET.get("cate")
    key_word = request.GET.get("key_word")
    if cate =="name":
        student_list= Student.objects.filter(name__contains = key_word)
    elif cate =="class":
        student_list= Student.objects.filter(clas__contains = key_word)
    else:
        student_list=[]
    return render(request,"student/index.html",{"student_list":student_list, "key_word":key_word})