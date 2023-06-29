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
    path("auth/", include("social_auth.urls")),
    path("contact-us/", include("contact.urls")),
    ]
