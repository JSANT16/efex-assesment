from .models import Student


class StudentRepository:
    @staticmethod
    def create_student(data: Student) -> Student:
        student = Student.objects.create(**data)
        return student

    @staticmethod
    def get_all_students() -> list[Student]:
        return Student.objects.all()

    @staticmethod
    def get_student_by_id(student_id: int):
        return Student.objects.filter(id=student_id).first()
    
    @staticmethod
    def update_student(student_id, data: Student) -> Student:
        student = Student.objects.filter(id=student_id).first()
        if student:
            for key, value in data.items():
                setattr(student, key, value)
            student.save()
        return student