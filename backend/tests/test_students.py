from faker import Faker
import pytest
from rest_framework.test import APIClient

from student.models import Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def faker():
    return Faker()

@pytest.fixture
def create_student(faker):
    def _create_student():
        student = Student.objects.create(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        date_of_birth=faker.date_of_birth(minimum_age=10, maximum_age=18),
        grade=faker.random_int(min=1, max=12),
        email=faker.email(),
        phone='+1234567890',
    )
        return student
    return _create_student

@pytest.mark.django_db
def test_create_student(client, faker):
    student_data = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "date_of_birth": faker.date_of_birth(minimum_age=10, maximum_age=18),
        "grade": faker.random_int(min=1, max=12),
        "email": faker.email(),
        "phone": '+1234567890',
    }

    response = client.post("/api/students/", student_data, format='json')
    assert response.status_code == 201
    assert Student.objects.count() == 1
    assert Student.objects.first().first_name == student_data["first_name"]

@pytest.mark.django_db
def test_get_student(client, create_student):
    student = create_student()
    response = client.get(f"/api/student/{student.id}/")
    assert response.status_code == 200
    assert response.data["first_name"] == student.first_name
    assert response.data["grade"] == student.grade

@pytest.mark.django_db
def test_update_student(client, create_student):
    student = create_student()
    updated_data = {
        "first_name": "Jane Doe",
        "phone": "+1234567890"
    }

    response = client.patch(f"/api/student/{student.id}/", updated_data, format='json')
    print(response.data)
    assert response.status_code == 200
    student.refresh_from_db()
    assert student.first_name == updated_data["first_name"]
    assert student.phone == updated_data["phone"]


@pytest.mark.django_db
def test_delete_student(client, create_student):
    student = create_student()
    response = client.delete(f"/api/student/{student.id}/")

    assert response.status_code == 204
    assert Student.objects.count() == 0