from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for blog with username,title,entry
class Blog(models.Model):
    username = models.CharField(max_length= 10)
    blog_title= models.CharField(max_length= 100)
    blog_entry = models.TextField(max_length=500000000)
    blog_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

# to display username on site
    def __str__(self):
        return self.username