<<<<<<< HEAD
from django.contrib import admin

from .models import Contact


class ContactModel(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


admin.site.register(Contact, ContactModel)
=======
from django.contrib import admin

from .models import Contact


class ContactModel(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


admin.site.register(Contact, ContactModel)
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
