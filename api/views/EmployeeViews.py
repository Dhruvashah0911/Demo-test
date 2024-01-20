from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from api.filters.employee_filters import EmployeeSearchOrderFilter
from api.models import Employee
from api.services.employee_services import validate_employee_age
from api.serializers.EmployeeSerializers import EmployeeSerializer,EmployeeAddSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.filter(is_deleted=False)
    serializer_class = EmployeeSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_class = EmployeeSearchOrderFilter


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
     
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeAddSerializer
    
    def perform_create(self, serializer):
        error_response = validate_employee_age(serializer)
        if error_response:
            return error_response

        serializer.save()

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_update(self, serializer):
        error_response = validate_employee_age(serializer)
        if error_response:
            return error_response

        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



