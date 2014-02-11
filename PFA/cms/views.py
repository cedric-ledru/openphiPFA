from django.shortcuts import render

# Create your views here.
def cms_index(request):
    return render(request, 'PFA/base.html', {})
