<<<<<<< HEAD
from django.urls import path, include
from .views import UserViewSet, Login, Register, BlogView, CommentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("details/", include(router.urls)),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("comment/", CommentView.as_view(), name="comment"),
]
=======
from django.urls import path, include
from .views import UserViewSet, Login, Register, BlogView, CommentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("details/", include(router.urls)),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("comment/", CommentView.as_view(), name="comment"),
]
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
