from django.urls import path, include

urlpatterns = [
    # Include all account-related routes (/accounts/register, /accounts/login, /accounts/logout)
    path("accounts/", include("accounts.urls")),

    # Include all task-related routes (/tasks/)
    path("tasks/", include("tasks.urls")),
]
