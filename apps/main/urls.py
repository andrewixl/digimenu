from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<slug>\w+)$', views.menu),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)