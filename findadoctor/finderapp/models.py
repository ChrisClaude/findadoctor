from django.db import models
from django.contrib.auth.models import User


class Hospital(models.Model):
    name = models.CharField(max_length=250, unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField
    hospital = models.ForeignKey(Hospital, related_name="findadoctor", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    patient = models.ForeignKey(User, related_name="findadoctor", on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, related_name="findadoctor", on_delete=models.CASCADE)
    date = models.DateTimeField('Date and Time Booked')

    def __str__(self):
        return self.patient.username + ' ' + str(self.date)
