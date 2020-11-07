from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('projetos/', include('projetos.urls')),
    path('admin/', admin.site.urls),
]
