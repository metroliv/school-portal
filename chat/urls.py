from django.urls import path
from . import views
from .views import start_video_call, join_video_call

urlpatterns = [
    path('chat/', views.chat_list, name='chat_list'),
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_chat, name='group_chat'),
    path('groups/new/', views.create_group, name='create_group'),
    path('start/', start_video_call, name='start_video_call'),
    path('join/<str:call_id>/', join_video_call, name='join_video_call'),
]

