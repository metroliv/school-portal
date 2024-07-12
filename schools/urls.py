from django.urls import path
from . import views
from .views import (
    SchoolListView, SchoolDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView,
    ClassListView, ClassDetailView, ClassCreateView, ClassUpdateView, ClassDeleteView,
    StreamListView, StreamDetailView, StreamCreateView, StreamUpdateView, StreamDeleteView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView
)

urlpatterns = [
    # School URLs
    path('schools/', SchoolListView.as_view(), name='school_list'),
    path('schools/add/', SchoolCreateView.as_view(), name='school_add'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('schools/<int:pk>/edit/', SchoolUpdateView.as_view(), name='school_edit'),
    path('schools/<int:pk>/delete/', SchoolDeleteView.as_view(), name='school_delete'),

    # Class URLs
    path('schools/<int:school_id>/classes/', ClassListView.as_view(), name='class_list'),
    path('schools/<int:school_id>/classes/add/', ClassCreateView.as_view(), name='class_add'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
    path('classes/<int:pk>/edit/', ClassUpdateView.as_view(), name='class_edit'),
    path('classes/<int:pk>/delete/', ClassDeleteView.as_view(), name='class_delete'),

    # Stream URLs
    path('classes/<int:class_id>/streams/', StreamListView.as_view(), name='stream_list'),
    path('classes/<int:class_id>/streams/add/', StreamCreateView.as_view(), name='stream_add'),
    path('streams/<int:pk>/', StreamDetailView.as_view(), name='stream_detail'),
    path('streams/<int:pk>/edit/', StreamUpdateView.as_view(), name='stream_edit'),
    path('streams/<int:pk>/delete/', StreamDeleteView.as_view(), name='stream_delete'),

    # Student URLs
    path('streams/<int:stream_id>/students/', StudentListView.as_view(), name='student_list'),
    path('streams/<int:stream_id>/students/add/', StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
