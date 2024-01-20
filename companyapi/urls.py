from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse



schema_view = get_schema_view(
    openapi.Info(
        title="basic API documentation",
        default_version='v1',
        description="Test documentation",
        terms_of_service="https://www.goggle.com/terms/",
        contact=openapi.Contact(email="contact@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', lambda request: HttpResponse('Welcome to EAFoods!', status=200), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include your app's URLs here
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

