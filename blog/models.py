from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name='')
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:12].strip() + ('...' if len(self.content) > 10 else '')
