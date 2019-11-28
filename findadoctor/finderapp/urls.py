from rest_framework import routers

from .api import BookingViewSet
from .api import DoctorViewset, HospitalViewset

router = routers.DefaultRouter()
router.register('api/bookings', BookingViewSet, 'bookings')
router.register('api/hospitals', HospitalViewset, 'bookings')
router.register('api/doctors', DoctorViewset, 'bookings')

urlpatterns = router.urls
