<<<<<<< HEAD
from django.urls import path

from .views import ContactView

urlpatterns = [
    path("", ContactView.as_view(), name="contact-us"),
]
=======
from django.urls import path

from .views import ContactView

urlpatterns = [
    path("", ContactView.as_view(), name="contact-us"),
]
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
