from django import forms
from codepage.models import Code, TestCase


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code_file', ]


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['input', 'output']
