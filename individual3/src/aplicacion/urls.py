from django.urls import path
from aplicacion.views import landing_page
from aplicacion.views import clients, imagenes



urlpatterns=[
    path('', landing_page, name='landing_page'),
    path('clients/', clients, name='clients'),
    path('imagenes/', imagenes,name='imagenes'),

]
