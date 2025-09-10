from django.urls import path
from . import views

app_name = 'requisicoes'

urlpatterns = [
    path('nova/', views.nova_requisicao, name='nova'),
    path('<int:pk>/', views.detalhe_requisicao, name='detalhe'),
    path('', views.listar_requisicoes, name='listar'),
    path('<int:pk>/atender/', views.atender_requisicao, name='atender'),
]         