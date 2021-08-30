from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_primary(m):
    measurement_pk = Measurement.objects.filter(pk=m)
    return measurement_pk

def upd_measurement_by_primary(m, p):
    measurement_pk = Measurement.objects.filter(pk=m)
    measurement_pk.update(value=p)

def del_measurement_by_primary(m_pk):
    measurement_pk = Measurement.objects.filter(pk=m)
    measurement_pk.delete()

