from . import views
from django.urls import include, path

urlpatterns={
    path('',views.pagina_inicio,name='inicio'),
    path('ingresar_rut',views.ingresar_rut,name='ingresar_rut'),
    path('presionar_entrada/<int:id>',views.entrada,name='presionar_entrada'),
     path('presionar_salida/?P<id>',views.salida,name='presionar_salida')
}