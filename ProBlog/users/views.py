from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
#Using the user creating form that already exists in django
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #Django does the backend check with UserCreationForm automatically
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created Successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required      #its a decorator that requires user to be logged in to be able to call this function
def profile(request):
    return render(request, 'users/profile.html')
