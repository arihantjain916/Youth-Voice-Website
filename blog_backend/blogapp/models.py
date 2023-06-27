from django.db import models
import uuid
from django.contrib.auth.models import User


class BlogBase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BlogBase):
    title = models.CharField(max_length=2000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")

    # for image: models.ImageField(upload_to = "blogs")
    # This will create a new folder name blogs
    # in the root directory of your project and store all images there

    def __str__(self):
        return self.title


class CommentBase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comments(CommentBase):
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comment")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    comment = models.TextField()
    is_verified = models.BooleanField(default=False)

    def type(self):
        return self.commenter
