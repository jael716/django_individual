from django.urls import path
from aplicacion.views import landing_page

urlpatterns=[
    path('', landing_page, name='landing_page'),

]
