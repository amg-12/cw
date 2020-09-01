from django.shortcuts import render

from .models import *


def index(request):
    return render(request, 'cv/index.html',
        {'details': Details.objects.first(),
         'links': Link.objects.all(),
         'education': School.objects.all(),
         'career': Work.objects.all(),
         'achievements': Achievement.objects.all()
        })
