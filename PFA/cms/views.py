from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cms.models import Document

# Create your views here.
@login_required
def home(request):
    docs = request.user.document_set.all()
    return render(request, 'cms/base.html', locals())

@login_required
def create(request):
    return render(request, 'cms/create.html', {})
