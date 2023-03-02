from . import views
from django.urls import include, path

urlpatterns={
    path('',views.pagina_inicio,name='inicio')
}