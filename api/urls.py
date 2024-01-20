from django.urls import path
from api.views.CompanyViews import CompanyListView
from api.views.EmployeeViews import EmployeeListCreateView,EmployeeDetailView,EmployeeListView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('employee/add', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
    
    
   
