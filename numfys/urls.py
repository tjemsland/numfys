from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^modules/', include('module.urls')),
    url(r'^examples/', include('example.urls')),
    url(r'^admin/', admin.site.urls),
]
