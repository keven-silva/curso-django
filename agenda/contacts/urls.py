from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.template_contact, name='template_contact'),
    path('busca/', views.busca, name='busca')
]

