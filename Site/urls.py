from django.urls import path
from Site import views
#lista urlpatterns global do projeto
urlpatterns = [
    path('', views.index, name = "index"),
    path('produtos', views.produto_lista, name="produto_lista"), #listagem de todos os produtos
    path('produto', views.produto_detalhe, name="produto_detalhe"), #detalhe de um produto específico
    path('sobre-a-empresa', views.institucional, name="institucional"), #sobre a empresa
    path('cadastro', views.cadastro, name="cadastro"), #cadastro
    path('contato', views.contato, name="contato"), #contato
]