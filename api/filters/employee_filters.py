from django_filters import rest_framework as filters



class EmployeeSearchOrderFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains', field_name='first_name')  
    last_name = filters.CharFilter(lookup_expr='icontains', field_name='last_name')  
    email_address = filters.CharFilter(lookup_expr='icontains', field_name='email_address')  

    