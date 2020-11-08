from django.contrib import admin
from django.urls import include, path
from .views import raiz

urlpatterns = [
    path('', raiz),
    path('projetos/', include('projetos.urls')),
    path('admin/', admin.site.urls),
]
