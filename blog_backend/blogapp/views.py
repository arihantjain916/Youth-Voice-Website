from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Blog, Comments
from django.contrib.auth.models import User
from .serializers import (
    BlogSerializer,
    UserLoginSerializer,
    UserCreateSerializer,
    UserSerializer,
    BlogViewSerializer,
    CommentSerializer,
)
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator


# Create new user
class Register(APIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request):
        """Register a new user"""
        data = request.data
        serializer_class = UserCreateSerializer(data=data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        response = {"data": serializer_class.data}
        return Response(
            {
                "message": "User Register Successfully",
                "data": response,
                "status": HTTP_200_OK,
            }
        )


# Login user
class Login(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            data = request.data
            serializer_class = UserLoginSerializer(data=data)
            if serializer_class.is_valid(raise_exception=True):
                username = serializer_class.data["username"]
                password = serializer_class.data["password"]

                # Check if the user is exist
                user = User.objects.filter(username=username).exists()
                if user is None:
                    return Response({"message": "User do not exist"})

                # Authenticate the user
                user = authenticate(username=username, password=password)
                print(user)
                if user is None:
                    return Response(
                        {
                            "status": HTTP_400_BAD_REQUEST,
                            "Message": "Wrong Password",
                        }
                    )
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "username": serializer_class.data["username"],
                    }
                )

            return Response(
                {"Message": serializer_class.errors, "status": HTTP_400_BAD_REQUEST}
            )

        except Exception as e:
            print(e)
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


# CRUD the blog
class BlogView(APIView):
    queryset = User.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            blogs = Blog.objects.filter(author=request.user)
            if request.GET.get("search"):
                search = request.GET.get("search")
                blogs = blogs.filter(
                    Q(title__icontains=search) | Q(content__icontains=search)
                )

            serializer_class = BlogSerializer(blogs, many=True)
            return Response(
                {
                    "data": serializer_class.data,
                    "message": "Blogs Fetched Successfully",
                    "status": HTTP_200_OK,
                }
            )
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            data = request.data
            data["author"] = request.user.id
            serializer_class = BlogSerializer(data=data)
            if serializer_class.is_valid(raise_exception=True):
                serializer_class.save()
            return Response(
                {
                    "data": serializer_class.data,
                    "message": "Blog Created Successfully",
                    "code": 201,
                }
            )
        except Exception as e:
            print(e)
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            data = request.data
            data["author"] = request.user.id
            serializer_class = BlogSerializer(data=data)
            blog = Blog.objects.filter(id=data.get("id"))
            if not blog.exists():
                return Response(
                    {
                        "data": {},
                        "message": "Blog not exist",
                        "code": HTTP_400_BAD_REQUEST,
                    }
                )
            if request.user != blog[0].author:
                return Response(
                    {
                        "data": {},
                        "message": "You are not authorized to do this operations",
                        "code": HTTP_400_BAD_REQUEST,
                    }
                )
            serializer_class = BlogSerializer(blog[0], data=data, partial=True)
            if serializer_class.is_valid(raise_exception=True):
                serializer_class.save()
            return Response(
                {
                    "data": serializer_class.data,
                    "message": "Blog Updated Successfully",
                    "code": 201,
                }
            )
        except Exception as e:
            print(e)
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            data["author"] = request.user.id
            serializer_class = BlogSerializer(data=data)
            blog = Blog.objects.filter(id=data.get("id"))
            if not blog.exists():
                return Response(
                    {
                        "data": {},
                        "message": "Blog not exist",
                        "code": HTTP_400_BAD_REQUEST,
                    }
                )
            if request.user != blog[0].author:
                return Response(
                    {
                        "data": {},
                        "message": "You are not authorized to do this operations",
                        "code": HTTP_400_BAD_REQUEST,
                    }
                )
            blog[0].delete()
            return Response(
                {
                    "data": {},
                    "message": "Blog Deleted Successfully",
                    "code": 201,
                }
            )
        except Exception as e:
            print(e)
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


# Throw User
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # user/{userid}/blog
    @action(detail=True, methods=["get"])
    def blogs(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            blogs = Blog.objects.filter(author=user)
            serializer_class = BlogViewSerializer(
                blogs, many=True, context={"request": request}
            )
            return Response({"blogs": serializer_class.data})
        except Exception:
            return Response(
                {"error": "Blog does not exist"}, status=HTTP_400_BAD_REQUEST
            )


# List the blog
class PublicBlog(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.all().order_by("?")

            if request.GET.get("search"):
                search = request.GET.get("search")
                blogs = blogs.filter(
                    Q(title__icontains=search) | Q(content__icontains=search)
                )
            page_number = request.GET.get("page", 1)
            paginator = Paginator(blogs, 8)

            serializer_class = BlogSerializer(paginator.page(page_number), many=True)
            return Response(
                {
                    "data": serializer_class.data,
                    "message": "Blogs Fetched Successfully",
                    "status": HTTP_200_OK,
                }
            )
        except Exception as e:
            return Response({"message": "Something went wrong or invalid page"})


# Comment View
class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # Get verified comment
    def get(self, request):
        try:
            data = request.data
            comment = Comments.objects.filter(blog=data.get("blog"))

            # if not comment.is_verified:
            #     return Response({
            #         "message": "Only verified contents shown"
            #     })
            serializer_class = CommentSerializer(comment, many=True)
            return Response(
                {
                    "data": serializer_class.data,
                    "message": "Comment Fetched Successfully",
                    "status": HTTP_200_OK,
                }
            )
        except Exception as e:
            print(e)
            return Response({"message": str(e), "data": {}})

    # Create comment
    def post(self, request):
        try:
            data = request.data
            data["commenter"] = request.user.id
            serializer_class = CommentSerializer(data=data)
            blog = Blog.objects.filter(id=data.get("blog")).exists()
            if not blog:
                return Response(
                    {
                        "data": {},
                        "message": "Blog not exist",
                        "code": HTTP_400_BAD_REQUEST,
                    }
                )
            if serializer_class.is_valid(raise_exception=True):
                serializer_class.save()
                return Response(
                    {
                        "data": serializer_class.data,
                        "message": "Comment Post Successfully",
                        "code": 201,
                    }
                )
        except Exception as e:
            print(e)
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
