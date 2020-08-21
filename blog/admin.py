from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['content']

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.author = request.user.username
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
