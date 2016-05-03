from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^modules/', include('notebook.urls_module')),
    url(r'^examples/', include('notebook.urls_example')),
    url(r'^search/', include('search.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The pattern has to be at the end of the urlpatterns
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
