from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Doctor, Hospital, Patient, Booking
from .serializers import BookingSerializer
from .serializers import PatientSerializer, RegisterDoctorSerializer, HospitalSerializer


# Booking Viewset
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def get_queryset(self):
    #     return self.request.user.bookings.all()

    # def perform_create(self, serializer):
    #     patient = Patient(self.request.user)
    #     serializer.save(patient=patient)


class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    queryset = Doctor.objects.all()
    serializer_class = RegisterDoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HospitalViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
