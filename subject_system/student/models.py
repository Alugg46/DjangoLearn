from django.db import models

# Create your models here.

class Clas(models.Model):
    name = models.CharField(max_length=32, verbose_name="班级名称")

    class Meta:
        db_table = "db_class"

class Course(models.Model):
    title = models.CharField(max_length=32, verbose_name="课程名称")
    credit = models.IntegerField(verbose_name="学分", default=3)
    teacher = models.CharField(max_length=32,default="2")
    classTime = models.CharField(max_length=32,default="3")
    classAddr = models.CharField(max_length=32,default="6")

    class Meta:
        db_table = "db_course"

class Student(models.Model):
    sex_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄", default=18)
    sex = models.SmallIntegerField(choices=sex_choices)
    birthday = models.DateTimeField()

    #一对多关系:在数据库中创建一个管理字段:clas_id
    clas = models.ForeignKey("Clas", related_name="student_list", on_delete=models.CASCADE, db_constraint=False)

    #多对多关系：创建第三张关系表
    courses = models.ManyToManyField("Course", related_name="course_list", db_table="db_student2course")

    #一对一关系：建立管理字段,在数据库中生成关联字段
    stu_detail = models.OneToOneField("StudentDetail", related_name="info_list", on_delete=models.CASCADE, null=True,blank=True)

    class Meta:
        db_table = "db_student"

class StudentDetail(models.Model):
    tel = models.CharField(max_length=11)
    addr = models.CharField(max_length=32)

    class Meta:
        db_table = "db_stu_detail"