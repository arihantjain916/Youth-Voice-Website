from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ["title"]
    list_filter = ["date_created"]

admin.site.register(Blog, BlogAdmin)

