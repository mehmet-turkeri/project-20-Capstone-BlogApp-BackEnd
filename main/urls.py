from django.contrib import admin
from django.urls import path, include
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title = "Blog Tracking API",
        default_version = "v1",
        description = "Blog API project allows you to write blog on the subject you want, read what others have written, and write comments on them.",
        terms_of_service = "#",
        contact = openapi.Contact(email="mehmet@clarusway.com"),
        # Change e-mail on this line!
        license = openapi.License(name="BSD License"),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # for swagger/redoc:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # for debug:
    # path('__debug__/', include('debug_toolbar.urls')),
    # go to users and blog/:
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
