from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text