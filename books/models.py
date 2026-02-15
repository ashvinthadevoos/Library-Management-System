from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    option=[
        ('N','Novel'),
        ('S','Short Story'),
        ('B','Biography'),
        ('E','Essays'),
        ('D','Drama'),
        ('P','Poetry')
    ]
    format=models.CharField(choices=option,max_length=1)
    GENERE=[
        ('F','Fantasy'),
        ('R','Romance'),
        ('H','Horror'),
        ('S','Science Fiction'),
        ('M','Mystery'),
        ('T','Thriller'),
        ('H','Historical Fiction'),
        ('A','Adventure')
    ]
    genre=models.CharField(choices=GENERE,max_length=1)
    price=models.BigIntegerField()
    date=models.DateField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class BookIssue(models.Model):
#     book=models.ForeignKey(Books,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     Issue_Date=models.DateTimeField(auto_now_add=True)
