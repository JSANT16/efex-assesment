from django.urls import path
from .views import StudentView, StudentGetByIdView

urlpatterns = [
    path('students/', StudentView.as_view(), name='studens'),
    path('students/<int:student_id>/', StudentGetByIdView.as_view(), name='student-detail'),
]
