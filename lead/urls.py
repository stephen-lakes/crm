from django.urls import path

from .views import add_lead, leads_list, leads_detail, leads_delete, leads_edit, convert_to_client

urlpatterns = [
    path('', leads_list, name='leads_list'),
    path('<int:pk>/', leads_detail, name='leads_detail'),
    path('<int:pk>/delete/', leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', leads_edit, name='leads_edit'),
    path('<int:pk>/convert/', convert_to_client, name='leads_convert'),
    path('add_lead/', add_lead, name='add_lead'),
]