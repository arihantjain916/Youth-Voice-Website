from django.urls import path, include
from .views import BlogViewSet, UserViewSet, Login
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"blog", BlogViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", Login.as_view(), name="login"),
] 

# companies => user
# companyid => user_id
#employees => blog
