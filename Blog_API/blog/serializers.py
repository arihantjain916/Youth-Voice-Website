from datetime import datetime
from django.db.models import Q
from requests import request
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Blog
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required = True, max_length=10)
    # set_password(password)
    # def create(self,email, password, name):
    #     user = User.objects.create(email)
    #     user = User.objects.create(name)
    #     user.set_password(password)
    #     user.save()

    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        email = data.get("email").lower()
        password = data.get("password")

        if not email and not password:
            raise ValidationError("Details not entered.")
        user = None

        user = User.objects.filter(Q(email=email) & Q(password=password)).distinct()
        if not user.exists():
            raise ValidationError("User credentials are not correct.")
        user = User.objects.get(email=email)

        data["token"] = uuid4()
        user.token = data["token"]
        user.save()
        return data

    class Meta:
        model = User
        fields = ("email", "password", "token")

        read_only_fields = ("token",)


class BlogSerializer(serializers.ModelSerializer):
    blog_id = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"
