from django.views.generic import ListView, DetailView

from notebook.models import Notebook


class NotebookListView(ListView):
    """Generic Django display list view."""
    model = Notebook


class NotebookDetailView(DetailView):
    """Generic Django display detail view. Not used yet, can be used when
    enabling comments to notebooks, e.g.
    """
    model = Notebook
