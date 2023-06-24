from django.contrib import admin
from .models import User, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ["title"]
    list_filter = ["date_created"]


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    search_fields = ["name"]


admin.site.register(User, UserAdmin)
admin.site.register(Blog, BlogAdmin)
