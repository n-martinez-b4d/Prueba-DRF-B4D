from django.db import models

# Create your models here.

# for post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    state = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)