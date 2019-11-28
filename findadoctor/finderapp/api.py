from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Doctor, Hospital, Booking
from .serializers import BookingSerializer
from .serializers import RegisterDoctorSerializer, HospitalSerializer


# Booking Viewset
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Doctor.objects.all()
    serializer_class = RegisterDoctorSerializer


class HospitalViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
