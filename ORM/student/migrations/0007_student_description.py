# Generated by Django 3.2 on 2021-10-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20211009_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(null=True, verbose_name='个性签名'),
        ),
    ]
