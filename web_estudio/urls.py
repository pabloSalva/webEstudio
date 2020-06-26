from django.urls import path

from . import views

app_name = 'web_estudio'

urlpatterns = [
    path('', views.index, name='index'),
    path('turnos',views.turnos, name='turnos'),
    path('civilycomercial',views.civil_comercial, name='civilycomercial'),
    path('laboral', views.laboral, name='laboral')
]