<<<<<<< HEAD
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Blog, Comments
from django.contrib.auth.models import User


# Register Serializer
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # name = serializers.CharField()
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=10)

    def create(self, validated_data):
        user = User.objects.create(
            # name=validated_data["name"],
            username=validated_data["username"].lower(),
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ("password", "username")


# Show all blogs of the user Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# Show all blog Serializer
class BlogViewSerializer(serializers.ModelSerializer):
    blog_id = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"


# Create blog Serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ["date_created", "date_updated"]


# Create comment
class CommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField()
    class Meta:
        model = Comments
        exclude = ["created_at"]

=======
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Blog, Comments
from django.contrib.auth.models import User


# Register Serializer
class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # name = serializers.CharField()
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=10)

    def create(self, validated_data):
        user = User.objects.create(
            # name=validated_data["name"],
            username=validated_data["username"].lower(),
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ("password", "username")


# Show all blogs of the user Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# Show all blog Serializer
class BlogViewSerializer(serializers.ModelSerializer):
    blog_id = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"


# Create blog Serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ["date_created", "date_updated"]


# Create comment
class CommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField()
    class Meta:
        model = Comments
        exclude = ["created_at"]

>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
