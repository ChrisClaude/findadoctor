from rest_framework import viewsets, permissions

from .models import Doctor, Hospital
from .serializers import BookingSerializer
from .serializers import RegisterDoctorSerializer, HospitalSerializer


# Booking Viewset
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = BookingSerializer

    def get_queryset(self):
        return self.request.user.bookings.all()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = RegisterDoctorSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]


class HospitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]
