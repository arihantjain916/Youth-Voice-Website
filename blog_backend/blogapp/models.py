from django.db import models
import uuid
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.URLField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=2000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    #for image: models.ImageField(upload_to = "blogs")
    # This will create a new folder name blogs
