from django.db import models

MAX = 14


class Details(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()


class Link(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.text


class School(models.Model):
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.name


class Achievement(models.Model):
    time = models.CharField(max_length=255)
    description = models.TextField()

    def __str__():
        return self.description[:MAX].strip() + ('...' if len(self.description) > MAX else '')
