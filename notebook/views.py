from django.shortcuts import render
from notebook.models import Notebook
import random

def module_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='M', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )

def example_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='E', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )

def random_notebook(request):
    notebooks = Notebook.objects.filter(published=1)
    randNotebook = None

    if len(notebooks) > 0:
        randIndex = random.randint(0, len(notebooks)-1)
        randNotebook = notebooks[randIndex]

    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': [randNotebook]})
