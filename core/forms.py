from django import forms
from .models import Link

class FormLinks(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url_original']