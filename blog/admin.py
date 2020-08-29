from django.contrib import admin
from django import forms

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'pin']

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            #'pin': forms.BooleanField(attrs={'style' : 'color:yellow'})
        }
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.author = request.user.username
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
