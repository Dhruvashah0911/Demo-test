from django.db import models 

from rest_framework import generics

from api.models import Company
from api.serializers.CompanySerializers import CompanySerializer

    
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.annotate(total_employees_count=models.Count('employee'))
    serializer_class = CompanySerializer






