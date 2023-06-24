from django.db import models


class User(models.Model):
    class Usertype(models.TextChoices):
        admin = ("admin")
        user = "user"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    token = models.CharField(max_length=500, null=True, default="")
    type = models.CharField(
        max_length=5, choices=Usertype.choices, default=Usertype.user
    )

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2000)
    content = models.TextField(default="")
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
