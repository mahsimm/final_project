from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shopping', ShoppingViewSet,basename='shopping')
urlpatterns = [
    path('shop/', Shop.as_view(), name="shop"),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
