from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Added token field

    def save(self, *args, **kwargs):
        if not self.pk and not self.token:  # Check if token is not set
            self.token = uuid.uuid4()  # Generate token only for new users
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
