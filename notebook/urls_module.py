from django.conf.urls import url
from notebook.views import NotebookListView, NotebookDetailView


urlpatterns = [
    url(r'^$', NotebookListView.as_view(
        template_name='notebook/module_list.html')),
    # Not used yet, can be used when enabling comments to notebooks, e.g.
    url(r'^(?P<slug>[-\w]+)/$', NotebookDetailView.as_view(
        template_name='notebook/module_detail.html')),
]
