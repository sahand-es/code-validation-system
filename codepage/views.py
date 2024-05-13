from django.shortcuts import render
from django.utils.safestring import mark_safe
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_for_filename
from pygments import highlight

from codepage.forms import CodeForm, TestCaseForm
from codepage.models import TestCase

highlighted_html = ''  # Global variable to store highlighted HTML

def code_page(request):
    global highlighted_html  # Declare highlighted_html as global

    # Get all test cases
    test_cases = TestCase.objects.all()

    # Handle POST request
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Handle code upload
        if form_type == 'code-upload':
            code_form = CodeForm(request.POST, request.FILES)
            if code_form.is_valid():
                code = code_form.save(commit=False)
                code_file = code.code_file

                # Highlight the code
                lexer = get_lexer_for_filename(code_file.name)
                formatter = HtmlFormatter(style='monokai', noclasses=True, nobackground=True, linenos=False, full=True)
                highlighted_html = highlight(code_file.file.read(), lexer, formatter)

        # Handle test case upload
        elif form_type == 'test-case-upload':
            test_case_form = TestCaseForm(request.POST)
            if test_case_form.is_valid():
                test_case = test_case_form.save()

        elif form_type == 'test-case-delete':
            test_case_id = request.POST.get('test_case_id')
            test_case = TestCase.objects.get(id=test_case_id)
            test_case.delete()

    # Render the template
    return render(request, "html/main/codepage.html", {'code_html': mark_safe(highlighted_html), 'test_cases': test_cases})
