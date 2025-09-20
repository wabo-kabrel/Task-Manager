from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Task model - represents a single task belonging to a user
class Task(models.Model):
    title = models.CharField(max_length=200)  # Task title
    is_completed = models.BooleanField(default=False)  # Status: completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when created
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True,           # Allow owner to be empty
        blank=True           # Allow blank in forms / serializers
    )
    # Now tasks can exist without an associated user
    # If a user is deleted, their tasks are still deleted if owner exists

    def __str__(self):
        return self.title  # String representation in admin panel
