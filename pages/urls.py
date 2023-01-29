from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('essay-writing/', views.essay_writing, name='essay_writing'),
    path('paraphrase/', views.paraphrase, name='paraphrase'),
    path('generate-images/', views.generate_images, name='generate_images'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
