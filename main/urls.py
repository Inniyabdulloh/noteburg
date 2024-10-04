from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='home'),
    path('create-client/', views.CreateClientView.as_view(), name='create-client'),
]