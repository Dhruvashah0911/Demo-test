from rest_framework import serializers
from api.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'company', 'profile_img ', 'profile_img _thumbnail', 'email_address', 'created_at']

        

