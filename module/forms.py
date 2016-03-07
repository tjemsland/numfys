from django import forms


class UploadModuleForm(forms.Form):
    """Data from this form is available as e.g.
    request.FILES['file_html']. See Django documentation at
    https://docs.djangoproject.com/en/dev/topics/http/file-uploads/
    """
    title = forms.CharField(max_length=50)
    file_html = forms.FileField()
    file_ipynb = forms.FileField()
