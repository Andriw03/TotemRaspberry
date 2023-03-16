from . import views
from django.urls import include, path

urlpatterns=[
    path('',views.pagina_inicio,name='inicio'),
    path('presionar_entrada/<str:rut>',views.entrada,name='presionar_entrada'),
    path('presionar_salida/<str:rut>',views.salida,name='presionar_salida'),
    path('ingresar-rut/',views.ingresar_rut,name='ingresar_rut'),
]