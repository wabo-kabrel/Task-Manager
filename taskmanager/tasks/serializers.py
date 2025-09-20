from rest_framework import serializers
from .models import Task

# Serializer converts Task model to JSON and vice versa
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Add this line

    class Meta:
        model = Task
        fields = ["id", "title", "is_completed", "created_at", "owner"]  # Add "owner"
