from .logic.logic_measurements import get_all_measurements, get_measurement_by_primary, del_measurement_by_primary, upd_measurement_by_primary
from django.http import HttpResponse
from django.core import serializers
from .models import Measurement

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement_primary(request, m):
    measurement = get_measurement_by_primary(m)
    measurement_object = serializers.serialize('json', measurement)
    return HttpResponse(measurement_object, content_type='application/json')

def upd_measurement_primary(request, m, p):
    measurement = upd_measurement_by_primary(m, p)
    measurement_primary = get_measurement_primary(request, m)
    return HttpResponse(measurement_primary, content_type='application/json')

def del_measurement_primary(request, m):
    measurement_primary = get_measurement_by_primary(request, m)
    measurement = del_measurement_by_primary(m)
    return HttpResponse(measurement_primary, content_type='application/json')


