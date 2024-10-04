from .models import Student
from .repository import StudentRepository
from .serializers import StudentSerializer

class CreateStudentUseCase:
    def execute(self, data:Student) -> Student:
        student = StudentRepository.create_student(data)
        return StudentSerializer(student).data

class GetStudentsUseCase:
    def execute(self) -> list[Student]:
        students = StudentRepository.get_all_students()
        return StudentSerializer(students, many=True).data

class GetStudentByIdUseCase:
    def execute(self, student_id:int) -> Student | None:
        student = StudentRepository.get_student_by_id(student_id)
        return StudentSerializer(student).data if student else None
    
class UpdateStudentUseCase:
    def execute(self, student_id:int, data:Student) -> Student | None:
        student = StudentRepository.update_student(student_id, data)
        return StudentSerializer(student).data if student else None
