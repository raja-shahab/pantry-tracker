from django.contrib import admin
from django.urls import path
from pantry_tracker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pantry),
    path('delete_pantry/<id>', views.delete_pantry, name='delete_pantry'),
    path('update_pantry/<id>', views.update_pantry, name='update_pantry'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)