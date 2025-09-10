from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.lista_materiais, name='lista'),
    path('materiais/<int:pk>/', views.material_detalhe, name='detalhe'),
]