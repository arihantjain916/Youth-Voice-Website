<<<<<<< HEAD
from django.urls import path

from .views import GoogleSocialAuthView

urlpatterns = [
    path("google/", GoogleSocialAuthView.as_view(), name = "google-auth"),
]
=======
from django.urls import path

from .views import GoogleSocialAuthView

urlpatterns = [
    path("google/", GoogleSocialAuthView.as_view(), name = "google-auth"),
]
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
