from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from api.models import Employee
from api.serializers.EmployeeSerializers import EmployeeSerializer



class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email_address']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = self.get_custom_response(serializer.data)
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

       
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        
        return Response(serializer.data)

        


    def get_custom_response(self, data):
    
        custom_data = []
        for employee in data:
            custom_employee_data = {
                'full_name': employee['first_name'] + ' ' + employee['last_name'],
                'profile_pic': employee['profile_pic'],
                'profile_pic_thumbnail': employee['profile_pic_thumbnail'],
                'company_name': employee['company']['company_name'],
                'email_address': employee['email_address'],
            }
            custom_data.append(custom_employee_data)
        return custom_data
    

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer