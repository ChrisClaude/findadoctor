from rest_framework import routers

from .api import BookingViewSet
from .api import PatientViewSet, DoctorViewset, HospitalViewset

router = routers.DefaultRouter()
router.register('api/bookings', BookingViewSet, 'bookings')
router.register('api/hospitals', HospitalViewset, 'bookings')
router.register('api/doctors', DoctorViewset, 'bookings')
router.register('api/patients', PatientViewSet, 'bookings')

urlpatterns = router.urls
