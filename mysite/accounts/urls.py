from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('logout/', views.logout_view, name="auth_logout"),
    path('login/', views.login_view, name="auth_login"),
    path('register/', views.registration_view, name="auth_register"),
    re_path('activation/(?P<activation_key>\w+)/$', views.activation_view, name = 'activation_view'),
    path('show_account/', views.show_account, name = 'show_account')

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)