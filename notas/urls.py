# notas/urls.py
from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.listar_notas, name='listar'),            # Listagem de notas fiscais
    path('nova/', views.nova_nota_fiscal, name='nova'),     # Cadastrar nova nota
    path('<int:pk>/', views.detalhe_nota, name='detalhe'),  # Detalhe da nota
    path('adicionar-item/', views.adicionar_item_nota, name='adicionar_item_nota'),
]
