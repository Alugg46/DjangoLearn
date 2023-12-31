from django.db import models

# Create your models here.
'''

-- auto-generated definition
create table db_student
(
    id       int auto_increment primary key,
    name     varchar(32) not null,
    age      smallint(6) not null,
    sex      smallint(6) not null,
    birthday date        not null,
    constraint name
        unique (name)
);

'''


class Student(models.Model):
    sex_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )

    # id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄",default=18)  # 年龄
    sex = models.SmallIntegerField(choices=sex_choices)
    birthday = models.DateField()

    classmate = models.CharField(max_length=32,verbose_name="班级" ,default="python脱产12期")

    description = models.TextField(null=True,verbose_name="个性签名")

    chinese_score = models.IntegerField(default=100)
    math_score = models.IntegerField(default=100)

    class Meta:
        db_table = "db_student"

    def __str__(self):
        return self.name



