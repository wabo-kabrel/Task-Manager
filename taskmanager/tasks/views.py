# tasks/views.py

# Import DRF's Response class for returning JSON responses
from rest_framework.response import Response  

# Import APIView, which allows us to create class-based API views
from rest_framework.views import APIView  

# Import DRF permissions to restrict access to authenticated users
from rest_framework import permissions  

# Import the model we want to expose via API
from .models import Task  

# Import the serializer we defined to convert Task objects <-> JSON
from .serializers import TaskSerializer  


# =======================
# LIST + CREATE TASK API
# =======================
class TaskListView(APIView):
    """
    GET  -> List all tasks
    POST -> Create a new task
    """

    # Remove authentication for testing purposes
    permission_classes = [permissions.AllowAny]

    # permission_classes = [permissions.IsAuthenticated]    # Apply authentication (Optional)

    def get(self, request):
        # Fetch all tasks from the database
        tasks = Task.objects.all()

        # Serialize tasks into JSON (many=True since it's a list)
        serializer = TaskSerializer(tasks, many=True)

        # Return the serialized data as JSON
        return Response(serializer.data)

    def post(self, request):
        # Deserialize the incoming request data into a Task object
        serializer = TaskSerializer(data=request.data)

        # Validate the data (check required fields, types, etc.)
        if serializer.is_valid():
            # Save the new Task to the database
            # Normally, we would assign the logged-in user as owner:
            # serializer.save(owner=request.user)
            # But since authentication is disabled for testing, we leave owner blank:
            serializer.save(owner=None)  

            # Return the saved task with 201 Created status
            return Response(serializer.data, status=201)

        # If validation fails, return errors with 400 Bad Request
        return Response(serializer.errors, status=400)


# =======================
# RETRIEVE + UPDATE + DELETE API
# =======================
class TaskDetailView(APIView):
    """
    GET    -> Retrieve a single task by ID
    PUT    -> Update an existing task
    DELETE -> Delete a task
    """
    # permission_classes = [permissions.IsAuthenticated]    # Apply authentication (Optional)

    # Remove authentication for testing purposes
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        """
        Helper method: fetch a Task by its primary key (ID).
        Returns None if not found.
        """
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        # Fetch task by ID
        task = self.get_object(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=404)

        # Serialize and return task as JSON
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        # Fetch task by ID
        task = self.get_object(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=404)

        # Deserialize request data into existing task
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            # Save updates to DB
            serializer.save()
            return Response(serializer.data)

        # If invalid, return errors
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        # Fetch task by ID
        task = self.get_object(pk)
        if task is None:
            # Return 404 if task doesn't exist
            return Response({"error": "Task not found"}, status=404)

        # Delete the task from DB
        task.delete()

        # Return 200 OK with a message confirming deletion
        return Response({"message": "Task deleted successfully"}, status=200)
