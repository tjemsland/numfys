from django.shortcuts import render
from notebook.models import Notebook


def module_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='M', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )


def example_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='E', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )
