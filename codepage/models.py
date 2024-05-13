from django.core.exceptions import ValidationError
from django.db import models
import os


def validate_code_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.cpp', '.c', '.java', '.py']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File not supported!')


class Code(models.Model):
    code_file = models.FileField(upload_to='', validators=[validate_code_file_extension])


class TestCase(models.Model):
    input = models.TextField()
    output = models.TextField()


