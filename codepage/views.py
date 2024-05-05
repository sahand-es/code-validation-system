from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from pygments.formatters.html import HtmlFormatter

from codepage.forms import CodeForm
from pygments.lexers import get_lexer_for_filename
from pygments import highlight
from pygments.formatters import html


def code_page(request):
    ctx = dict()
    ctx['content'] = 'print(hello World)'
    ctx['lang'] = 'python'
    if request.method == 'POST':
        code_form = CodeForm(request.POST, request.FILES)
        if code_form.is_valid():
            code = code_form.save()
            code_file = code.code_file

            lexer = get_lexer_for_filename(code_file.name)
            formatter = HtmlFormatter(style='monokai', noclasses=True, nobackground=True, linenos=False, full=True)
            highlighted_html = highlight(code_file.file.read(), lexer, formatter)
            return render(request, "html/main/codepage.html", {'code_html': mark_safe(highlighted_html)})

        else:
            print(code_form.errors)

    return render(request, "html/main/codepage.html", {})

# def upload_code(request):
#     if request.method == 'POST':
#         code_form = CodeForm(request.POST, request.FILES)
#         if code_form.is_valid():
#             code_form.save()
#             return load_page(request)
