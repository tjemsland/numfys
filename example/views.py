from django.views.generic import ListView, DetailView
from django.utils import timezone

from example.models import Example


class ExampleListView(ListView):
    """Generic Django display view. Relevant documentation at
    https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
    """

    model = Example

    def get_context_data(self, **kwargs):
        context = super(ExampleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ExampleDetailView(DetailView):

    model = Example

    def get_context_data(self, **kwargs):
        context = super(ExampleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
