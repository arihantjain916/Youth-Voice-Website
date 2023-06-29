from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name + " - " + str(self.email)
