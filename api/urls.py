from django.urls import path
from api.views.CompanyViews import CompanyListView
from api.views.EmployeeViews import EmployeeListView,EmployeeDetailView



urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('employee-list/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
     
   
]