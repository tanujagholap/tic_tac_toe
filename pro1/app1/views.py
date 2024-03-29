from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    template_name = 'app1/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('tic_url')
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('signup_url')


def signup_view(request):
    form = UserCreationForm()
    template_name = 'app1/signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request, template_name, context={'form': form})


def cpass_view(request):
    template_name = 'app1/cpass.html'
    if request.method == 'POST':
        new = request.POST['new']
        old = request.POST['old']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, template_name)


@login_required(login_url='login_url')
def tic_view(request):
    template_name = 'app1/index.html'
    return render(request, template_name)