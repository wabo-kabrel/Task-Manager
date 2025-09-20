# View for user registration

from django.contrib.auth.forms import UserCreationForm    # Importing the built-in user creation form
from django.contrib.auth import login    # Importing the login function to log in users
from django.shortcuts import render, redirect    # Importing render and redirect functions for handling HTTP requests

def register(request):
    if request.method == "POST":  # If the user submitted the registration form
        form = UserCreationForm(request.POST)  # Populate form with submitted data
        if form.is_valid():  # Check if form passes validation
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user immediately after registration
            return redirect("task_list")  # Redirect to task list page
    else:
        form = UserCreationForm()  # If it's a GET request, show an empty registration form

    # Render the registration template and pass the form to it
    return render(request, "accounts/register.html", {"form": form})