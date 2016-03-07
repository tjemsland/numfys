from django.conf.urls import url

from example.views import ExampleListView, ExampleDetailView


urlpatterns = [
    url(r'^$', ExampleListView.as_view(), name='example-list'),
    url(r'^(?P<slug>[-\w]+)/$', ExampleDetailView.as_view(),
        name='example-detail'),
]
