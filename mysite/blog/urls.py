from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('detail/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # path('detail/published/<int:pk>/', views.post_published, name='post_published'),
    path('detail/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('detail/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('detail/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]