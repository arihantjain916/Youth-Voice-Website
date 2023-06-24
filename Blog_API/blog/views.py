from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User, Blog
from .serializers import (
    BlogSerializer,
    UserLoginSerializer,
    UserCreateSerializer,
)
from rest_framework import viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    serializer_class = UserCreateSerializer

    # user/{userid}/blog
    @action(detail=True, methods=["get"])
    def blogs(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            blogs = Blog.objects.filter(author=user)
            serializer_class = BlogSerializer(
                blogs, many=True, context={"request": request}
            )
            return Response({"blogs": serializer_class.data})
        except Exception:
            return Response({
                "error":"Blog does not exist"
            },status=HTTP_400_BAD_REQUEST)


class Login(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


# Create the blog
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("date_created")
    serializer_class = BlogSerializer
