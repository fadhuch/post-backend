from . import views
from django.urls import path,re_path





app_name = 'posts'
urlpatterns = [
    path('', views.posts, name='posts'),
    path('new/', views.new_posts, name='new_posts'),
    path('comments/', views.comments, name='comments'),
    path('new-comments/', views.new_comments, name='new_comments'),
    # path('current_user/', views.current_user, name='current_user'),
    # path('users/', views.user_list, name='user_list'),
    
]
