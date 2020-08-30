from django.db import models

MAX = 14


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, default="", verbose_name='')
    content = models.TextField(blank=True, default="", verbose_name='')
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    pin = models.BooleanField(default=False)

    def __str__(self):
        name = self.title if self.title else self.content
        return name[:MAX].strip() + ('...' if len(name) > MAX else '')
