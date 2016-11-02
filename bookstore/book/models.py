from django.db import models
from django.contrib import admin
# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=20)
    bookDetail = models.TextField(max_length=500)
    bookImage = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sellerID = models.IntegerField()
    course = models.CharField(max_length=20)
    teacher = models.CharField(max_length=5)
    pubDate = models.DateField(auto_now=True)
    state = models.IntegerField()

    def __str__(self):
        return self.bookName

admin.site.register(Book)
