from django import forms
from codepage.models import Code


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code_file',]
