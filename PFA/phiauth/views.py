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
            next_url = form.cleaned_data["next_url"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if next_url != "":
                    return redirect(next_url)
                else:
                    return render(request, 'phiauth/signin.html', locals())                    
            else:
                error = True
                return render(request, 'phiauth/signin.html', locals())
    else:
        next_url =  request.GET.get("next", "")
        form = SignInForm(initial={'next_url': next_url})
        return render(request, 'phiauth/signin.html', locals())

def signOut(request):
    logout(request)
    return redirect(reverse('PFA.views.home'))

def profile(request):
    return render(request, 'phiauth/profile.html', {})
