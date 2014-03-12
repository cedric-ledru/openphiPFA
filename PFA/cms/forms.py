from django import forms

from cms.models import Document

class CreateDocumentForm(forms.Form):
    title = forms.CharField(max_length=100)
