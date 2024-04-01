from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add =True)
    blog_image = models.ImageField(upload_to = "blog_image")

