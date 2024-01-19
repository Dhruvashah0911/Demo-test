from rest_framework import serializers
from api.models import Company



class CompanySerializer(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField(source='id')
    class Meta:
        model = Company
        fields = ('id' , 'company_name' ,)

