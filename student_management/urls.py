from django.urls import path
from . import views

urlpatterns = [
    path('student_list', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/new/', views.student_create, name='student_create'),
    path('student/<int:pk>/edit/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:student_id>/enter-marks/', views.enter_marks, name='enter_marks'),
]
