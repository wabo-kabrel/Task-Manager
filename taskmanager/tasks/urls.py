# tasks/urls.py
from django.urls import path
from .views import TaskListView, TaskDetailView   # ✅ Correct names from views.py

urlpatterns = [
    # /tasks/api/  → list all tasks (GET) OR create new task (POST)
    path("api/", TaskListView.as_view(), name="task-list"),

    # /tasks/api/1/ → retrieve (GET), update (PUT), or delete (DELETE) task with id=1
    path("api/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
