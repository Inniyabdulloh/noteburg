from django.urls import path
from . import views


app_name = 'category'

urlpatterns = [
    path('create/', views.CreateCategoryView.as_view(), name='create'),
    path('list/', views.ListCategoryView.as_view(), name='list'),
    path('<int:id>/update/', views.UpdateCategoryView.as_view(), name='update'),
]
