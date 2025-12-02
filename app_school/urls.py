from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),

    # Student
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Subject
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/', views.SubjectCreateView.as_view(), name='subject_add'),
    path('subjects/<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject_edit'),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),

    # Teacher
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/add/', views.TeacherCreateView.as_view(), name='teacher_add'),
    path('teachers/<int:pk>/edit/', views.TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
]
