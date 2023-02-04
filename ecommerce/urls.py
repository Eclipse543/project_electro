from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from electro.views import create_checkout_session
from electro.views import success, cancel


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("electro.urls")),
    path("accounts/", include('django.contrib.auth.urls')),
    path('create-checkout-session/<int:pk>/', create_checkout_session, name='create-checkout-session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
