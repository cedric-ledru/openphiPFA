from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cms.models import Document
from cms.forms import CreateDocumentForm

# Create your views here.
@login_required
def home(request):
    docs = request.user.document_set.all()
    return render(request, 'cms/base.html', locals())

def display(request, user_login, id_doc):
    doc = Document.objects.get(id=id_doc)
    return render(request, 'cms/display.html', locals())

@login_required
def create(request):
    if request.method == "POST":
        form = CreateDocumentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            # create doc
            doc = Document(auth=request.user, content="", title=title)
            doc.save()
            return redirect('cms.views.home')
    else:
        form = CreateDocumentForm()
        return render(request, 'cms/create.html', locals())

@login_required
def update(request, id_doc):
    return render(request, 'cms/create.html', locals())
