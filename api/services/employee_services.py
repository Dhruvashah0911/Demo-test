from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

def validate_employee_age(serializer):
    birthdate = serializer.validated_data.get('birthdate')
    age = (datetime.now().date() - birthdate).days // 365
    if age < 18:
        return Response({"error": "Employee must be 18 years or older."}, status=status.HTTP_400_BAD_REQUEST)
