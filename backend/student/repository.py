from .models import Student


class StudentRepository:
    @staticmethod
    def create_student(data):
        student = Student.objects.create(**data)
        return student

    @staticmethod
    def get_all_students():
        return Student.objects.all()

    @staticmethod
    def get_student_by_id(student_id):
        return Student.objects.filter(id=student_id).first()
    
    @staticmethod
    def update_student(student_id, data):
        student = Student.objects.filter(id=student_id).first()
        if student:
            for key, value in data.items():
                setattr(student, key, value)
            student.save()
        return student