from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from module.models import Module
from module.forms import UploadModuleForm


class ModuleListView(ListView):
    """Generic Django display view. Relevant documentation at
    https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
    """

    model = Module

    def get_context_data(self, **kwargs):
        context = super(ModuleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ModuleDetailView(DetailView):

    model = Module

    def get_context_data(self, **kwargs):
        context = super(ModuleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def upload_module(request):
    """Save module HTML and ipynb files to database. Relevant
    documentation at
    https://docs.djangoproject.com/en/dev/topics/http/file-uploads/
    """
    if request.method == 'POST':
        form = UploadModuleForm(request.POST, request.FILES)
        if form.is_valid():
            # Save files to the location specified by upload_to
            newfilehtml = Module(file_html=request.FILES['file_html'])
            newfilehtml.save()
            newfileipynb = Module(file_ipynb=request.FILES['file_ipynb'])
            newfileipynb.save()
            return HttpResponseRedirect(reverse('module.views'))
    else:
        form = UploadModuleForm()
