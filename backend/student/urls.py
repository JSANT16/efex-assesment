from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDelete

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentRetrieveUpdateDelete.as_view(), name='student-retrieve-update-delete'),
]
