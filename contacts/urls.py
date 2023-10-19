from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.contact_add, name='contact_add'),
    path('<str:id_number>/update/', views.contact_update, name='contact_update'),
    path('<str:id_number>/delete/', views.contact_delete, name='contact_delete'),
]
