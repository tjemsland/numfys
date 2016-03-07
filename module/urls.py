from django.conf.urls import url

from module.views import ModuleListView, ModuleDetailView


urlpatterns = [
    url(r'^$', ModuleListView.as_view(), name='module-list'),
    url(r'^(?P<slug>[-\w]+)/$', ModuleDetailView.as_view(),
        name='module-detail'),
]
