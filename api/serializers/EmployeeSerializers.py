from datetime import datetime

from rest_framework import serializers

from api.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.company_name')
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'profile_img','first_name','last_name', 'profile_img_thumbnail', 'company_name', 'email_address', 'full_name', 'birthdate','company','is_deleted']
        # read_only_fields = ['company_id']
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
class EmployeeAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ['id', 'profile_img','first_name','last_name', 'profile_img_thumbnail', 'email_address', 'birthdate','company','is_deleted']
     

    def validate_birthdate(self, value):
        birthdate = value
        age = (datetime.now().date() - birthdate).days // 365
        if age < 18:
            raise serializers.ValidationError("Employee must be 18 years or older.")
        return value

    def validate_email_address(self, value):
        if not value:
            raise serializers.ValidationError("Email address is required.")
        elif not self.instance or (self.instance and self.instance.email_address != value):
            if Employee.objects.filter(email_address=value).exists():
                raise serializers.ValidationError("Email address must be unique.")
        return value



