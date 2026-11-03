from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fundacionPatrimonio/', views.catalogo_view, name='categoria'),
    path('lugar/<int:id>/', views.detalle_lugar, name='detalle'),
]
