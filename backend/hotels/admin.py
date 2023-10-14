from django.contrib import admin
from .models import Hotel,Rating,HotelReservation


# Register your models here.
admin.site.register(Hotel)
admin.site.register(Rating)
admin.site.register(HotelReservation)


