from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/user/', include('account.urls', namespace='account')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='BlogAPI')),

    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0",
    ), name='openapi-schema'),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()