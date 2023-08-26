# Generated by Django 4.1.7 on 2023-08-20 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_stu_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(db_table='db_student2course', related_name='course_list', to='student.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info_list', to='student.studentdetail'),
        ),
    ]