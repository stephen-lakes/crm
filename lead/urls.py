from django.urls import path

from .views import add_lead, leads, leads_detail, leads_delete, leads_edit

urlpatterns = [
    path('', leads, name='leads_list'),
    path('<int:pk>/', leads_detail, name='leads_detail'),
    path('<int:pk>/delete/', leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', leads_edit, name='leads_edit'),
    path('add_lead/', add_lead, name='add_lead'),
]