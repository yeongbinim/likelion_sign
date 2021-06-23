from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Blog(TimeStampModel):#글 하나하나 
    title = models.CharField(max_length= 100)
    body = models.TextField()

class Comment(models.Model):
    body = models.TextField()
    blog =  models.ForeignKey(Blog, on_delete=models.CASCADE)