# Generated by Django 4.1.7 on 2023-08-20 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_clas_alter_student_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_detail',
            field=models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info_list', to='student.studentdetail'),
        ),
    ]
