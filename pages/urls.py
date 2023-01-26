from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('essay-writing/', views.essay_writing, name='essay_writing'),
    path('paraphrase/', views.paraphrase, name='paraphrase'),
    path('generate-images/', views.generate_images, name='generate_images'),
    path('about/', views.about, name='about'),
]
