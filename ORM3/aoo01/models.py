from django.db import models

# Create your models here.
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key =True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # AuthorDetail one to one
    authorDetail = models.OneToOneField(to=AuthorDetail, on_delete=models.CASCADE)

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    #  Publish one to many
    publish = models.ForeignKey(to=Publish, on_delete=models.CASCADE)

    # Author many to many
    authors = models.ManyToManyField(to=Author)