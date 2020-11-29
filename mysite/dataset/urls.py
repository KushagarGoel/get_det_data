from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	re_path(r'^contribute/(?P<title>.*)/', views.upload, name="contribute"),
    path('upload/', views.create_dataset, name="create_dataset"),
	path('', views.home, name="home"),
    path('datasets/', views.all_dataset, name="all_datasets"),
    re_path(r'^datasets/(?P<title>.*)/', views.single, name="single_dataset"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
