from django.db import models
from users.models import User

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)