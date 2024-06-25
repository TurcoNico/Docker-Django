
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_frutas, name='lista_frutas'),
    path('fruta/nueva/', views.nueva_fruta, name='nueva_fruta'),
    path('fruta/<int:id>/', views.detalle_fruta, name='detalle_fruta'),
    path('fruta/<int:id>/editar/', views.editar_fruta, name='editar_fruta'),
    path('fruta/<int:id>/eliminar/', views.eliminar_fruta, name='eliminar_fruta'),
]