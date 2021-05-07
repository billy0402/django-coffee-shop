from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    if request.user.is_authenticated:
        return redirect('root')

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, '{} 您好，歡迎使用~'.format(user.username))
        return redirect('root')

    return render(request, 'users/register.html', {'form': form})
