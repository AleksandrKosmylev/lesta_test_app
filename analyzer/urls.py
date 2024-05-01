from django.urls import path
from analyzer.views import index
from django.conf.urls.static import static
from django.conf import settings
# from analyzer.views import IndexView


urlpatterns = [
    path('', index)
    # path('', IndexView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)