from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Open AI API",
        default_version='v1',
        description="Welcome to the world of Open Ai API's",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('chat/', views.chat, name='chat'),
    path('get_prompt/', views.get_prompt, name='get_prompt'),
    # path('get_chat/', views.get_chat, name='get_chat'),
    
]