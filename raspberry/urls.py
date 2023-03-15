from . import views
from django.urls import include, path

urlpatterns=[
    path('',views.pagina_inicio,name='inicio'),
    path('presionar_entrada/<int:id>',views.entrada,name='presionar_entrada'),
    path('presionar_salida/<int:id>',views.salida,name='presionar_salida'),
    path('ingresar-rut/',views.ingresar_rut,name='ingresar_rut'),
]