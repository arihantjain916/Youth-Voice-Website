<<<<<<< HEAD
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name + " - " + str(self.email)
=======
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name + " - " + str(self.email)
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
