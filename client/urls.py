from django.urls import path

from .views import clients_list, clients_detail, add_client, clients_delete, clients_edit

urlpatterns = [
    path('', clients_list, name='clients_list'),
    path('<int:pk>', clients_detail, name='clients_detail'),
    path('<int:pk>/delete/', clients_delete, name='clients_delete'),
    path('<int:pk>/edit/', clients_edit, name='clients_edit'),
    path('add_client/', add_client, name='add_client'),
]