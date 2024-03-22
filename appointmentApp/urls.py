from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees.views import EmployeeViewSet 
from departments.views import DepartmentViewSet
from customers.views import CustomerViewSet
from appointments.views import AppointmentViewSet
from authentication.urls import urlpatterns as auth_urls

BASE_URL = 'appointment-app/api/'

router = routers.SimpleRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('departments', DepartmentViewSet, basename='departments')
router.register('customers', CustomerViewSet, basename='customers')
router.register('appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include((router.urls, 'crud'))),
    path(BASE_URL + 'auth/', include((auth_urls, 'auth')))
]

urlpatterns += router.urls
