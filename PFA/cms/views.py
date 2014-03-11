from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.files import File

from cms.models import Document
#from cms.forms import CreateDocumentForm

# Create your views here.
@login_required
def home(request):
    docs = request.user.document_set.all()
    return render(request, 'cms/base.html', locals())

def display(request, user_login, id_doc):
    doc = Document.objects.get(id=id_doc)
    content = b""
    for line in doc.path:
            content += (line)
    return render(request, 'cms/display.html', locals())

@login_required
def create(request):
    return render(request, 'cms/create.html', locals())

@login_required
def update(request, id_doc):
    return render(request, 'cms/create.html', locals())
