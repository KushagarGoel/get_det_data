from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.create_article, name="create_article"),
    path('view_all/', views.view_article, name="view_article"),
    re_path('view_all/(?P<title>.*)/', views.single, name = 'article_single')


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)