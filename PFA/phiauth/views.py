from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, resolve

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from phiauth.forms import SignInForm

def signIn(request):
    error = False

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = SignInForm()
    return render(request, 'phiauth/signin.html', locals())

def signOut(request):
    logout(request)
    return redirect(reverse('PFA.views.home'))

def profile(request):
    return render(request, 'phiauth/profile.html', {})
