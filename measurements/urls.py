from measurements.logic.logic_measurements import del_measurement_by_primary, get_measurement_by_primary
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('id/<int:m>/', views.get_measurement_primary, name='measurementByPrimary'),
    path('delete/<int:m>/', views.del_measurement_primary, name='delMeasurementByPrimary'),
    path('update/<int:m>/value/<int:p>/', views.upd_measurement_primary, name='updMeasurementValue')
]