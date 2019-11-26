from django.contrib import admin
from .models import Booking, Doctor, Hospital

admin.site.register(Booking)
admin.site.register(Doctor)
admin.site.register(Hospital)

