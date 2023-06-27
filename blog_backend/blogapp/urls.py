from django.urls import path, include
from .views import UserViewSet, Login, Register, BlogView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("details/", include(router.urls)),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("blog/", BlogView.as_view(), name="blog"),
]
