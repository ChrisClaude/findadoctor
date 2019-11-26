from django.urls import path
from rest_framework import routers

from .api import BookingViewSet
from .api import DoctorViewset, HospitalViewset

router = routers.DefaultRouter()
router.register('api/bookings', BookingViewSet, 'bookings')
router.register('api/doctors', DoctorViewset, 'doctors')
router.register('api/hospitals', HospitalViewset, 'hospitals')

urlpatterns = router.urls
