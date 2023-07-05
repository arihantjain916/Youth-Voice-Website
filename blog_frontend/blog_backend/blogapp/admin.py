<<<<<<< HEAD
from django.contrib import admin
from .models import Blog, Comments


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ["title"]
    list_filter = ["date_created"]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["commenter", "blog","comment"]
    search_fields = ["commenter"]
    list_filter = ["created_at"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comments, CommentsAdmin)
=======
from django.contrib import admin
from .models import Blog, Comments


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ["title"]
    list_filter = ["date_created"]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["commenter", "blog","comment"]
    search_fields = ["commenter"]
    list_filter = ["created_at"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comments, CommentsAdmin)
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
