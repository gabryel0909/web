from django.urls import path
from . import views
urlpatterns = [
    path('inicio',views.inicio),
    path('p/', views.post_list, name='post-list'),
    path('post-create', views.post_create, name='post-create'),
    path('post-detail/<int:id>/', views.post_detail, name='post-detail'),
    path('post-delete/<int:id>/', views.post_delete, name='post-delete'),
    path('post-update/<int:id>', views.post_update, name='post-update'),
    path('post-search/',views.post_search,name='post-search'),
]