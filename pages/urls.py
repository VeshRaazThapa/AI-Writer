from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('plane-blog/<int:pk>/', views.BlogDetailPlaneView.as_view(), name='detail_blog_plane'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='detail_blog'),
    path('blog/<int:pk>/edit',views.BlogUpdateView.as_view(), name='update_blog'),
    path('essay-writing/', views.essay_writing, name='essay_writing'),
    path('paraphrase/', views.paraphrase, name='paraphrase'),
    path('text-completion/', views.text_completion, name='text_completion'),
    path('generate-images/', views.generate_images, name='generate_images'),
    path('about/', views.about, name='about'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
