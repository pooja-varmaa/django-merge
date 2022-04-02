from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post/edit/<slug:slug>/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('profile-edit/<str:email>',views.profile_edit, name='profile_edit'),
    path('profile/<str:email>', views.user_profile, name='user_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),    
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),          
    path('category/',  views.category_list, name='category_list'),
    path('tag/', views.tag_list,name='tag_list'),
    path('add/', views.add_category, name='add_category'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('signup', views.signup, name='signup'),
    path('', views.post_list, name='post_list'),
    
]



