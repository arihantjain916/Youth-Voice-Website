<<<<<<< HEAD
from .models import Contact
from rest_framework import serializers
from datetime import datetime


# Contact Serializers
class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=3, max_length=50)
    message = serializers.CharField(required=True, min_length=5, max_length=100)
    created_at = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Contact
        fields = ["name", "message", "email", "created_at"]
=======
from .models import Contact
from rest_framework import serializers
from datetime import datetime


# Contact Serializers
class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=3, max_length=50)
    message = serializers.CharField(required=True, min_length=5, max_length=100)
    created_at = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Contact
        fields = ["name", "message", "email", "created_at"]
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
