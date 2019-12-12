from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login


def login(request):
    return render(request, 'login.html')


# @require_http_methods('POST')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('hone.html')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def home(request):
    return render(request, 'home.html')
