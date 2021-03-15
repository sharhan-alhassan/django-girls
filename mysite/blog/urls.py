from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/add/', views.add, name='add'),
    path('detail/<int:pk>/edit/', views.edit, name='edit'),
    path('detail/<int:pk>/delete/', views.delete, name='delete')
]