from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)