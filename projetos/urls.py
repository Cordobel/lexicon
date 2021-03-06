from django.urls import path

from . import views

app_name = 'projetos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:projetos_id>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:projetos_id>/atividade/', views.atividade, name='atividade'),
]
