from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('talk.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
