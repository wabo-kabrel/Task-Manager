from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Task model - represents a single task belonging to a user
class Task(models.Model):
    title = models.CharField(max_length=200)  # Task title
    is_completed = models.BooleanField(default=False)  # Status: completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when created
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Foreign key means each Task belongs to one User
    # If the user is deleted, their tasks are deleted too (CASCADE)

    def __str__(self):
        return self.title  # String representation in admin panel
