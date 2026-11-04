from django.urls import path
from fundacionPatrimonio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('lugar/<int:id>/', views.detalle_lugar, name='detalle'),
    path('categoria/<int:id>/', views.filtro_categoria, name='filtro'),
]
