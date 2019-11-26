from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Booking, Doctor, Hospital


# Booking serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


# RegisterDoctor Serializer
class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'username', 'email', 'password', 'specialization', 'hospital')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        doctor = Doctor(user=user, specialization=validated_data['specialization'], hospital=validated_data['hospital'])
        doctor.save()

        return doctor
