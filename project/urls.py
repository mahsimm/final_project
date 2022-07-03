from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_page),
                  path('signup/', SignUp.as_view(), name="signup"),
                  path('signin/', SignIn.as_view(), name='signin'),
                  path('signout/', SignOut.as_view(), name='signout'),
                  path('dashboard/', include('dashboard.urls')),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "صفحه ادمین"
admin.site.site_title = "صفحه ادمین"
admin.site.index_title = "صفحه ادمین"
