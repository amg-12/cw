from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name='')
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
