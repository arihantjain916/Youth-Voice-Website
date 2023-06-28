from django.contrib import admin
from django.urls import path, include

class Admin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']

# Register your models here.
admin.site
urlpatterns = [
    path("admin/", admin.site.urls), 
    path("api/", include("blogapp.urls")),
    path("api/", include("social_auth.urls"))
    ]
