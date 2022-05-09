from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=400)