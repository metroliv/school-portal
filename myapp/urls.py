from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('counter/', views.counter, name='counter'),
    path('help/', views.help, name='help'),
    path('accounts/login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('categories/', views.category_list, name='category_list'),
    path('articles/<int:category_id>/', views.article_list, name='article_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),
    path('<str:room>/', views.chat_room, name='room'),
    
    path('my_model/', views.my_model, name='my_model'),
    path('settings/', views.user_settings, name='user_settings'),
    path('staff_list/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/new/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/edit/', views.staff_update, name='staff_update'),
    path('staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]
