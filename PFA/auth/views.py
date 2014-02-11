from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from auth.forms import UserForm

def signIn(request):
    error = False

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = UserForm()
    return render(request, 'auth/user.html', locals())

def signOut(request):
    logout(request)
    return redirect(reverse('PFA.views.home'))
