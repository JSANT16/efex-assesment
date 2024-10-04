from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .use_cases import  CreateStudentUseCase, GetStudentsUseCase, GetStudentByIdUseCase, UpdateStudentUseCase

class StudentView(APIView):
    def post(self, request):
        use_case = CreateStudentUseCase()
        result = use_case.execute(request.data)
        return Response(result, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        use_case = GetStudentsUseCase()
        result = use_case.execute()
        return Response(result, status=status.HTTP_200_OK)

class StudentGetByIdView(APIView):
    def get(self, request, student_id):
        use_case = GetStudentByIdUseCase()
        result = use_case.execute(student_id)
        if result:
            return Response(result, status=status.HTTP_200_OK)
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, student_id):
        use_case = UpdateStudentUseCase()
        result = use_case.execute(student_id, request.data)

        if isinstance(result, dict) and 'error' in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        elif result:
            return Response(result, status=status.HTTP_200_OK)
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)