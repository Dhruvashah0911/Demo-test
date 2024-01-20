from rest_framework import serializers
from api.models import Company



class CompanySerializer(serializers.ModelSerializer):
    total_employees_count = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ['id', 'company_name', 'is_deleted', 'total_employees_count']

