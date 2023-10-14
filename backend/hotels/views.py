from .models import Hotel, Rating, HotelReservation
from .serializers import HotelSerializer, RatingSerializer, HotelReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class HotelReservationViewSet(viewsets.ModelViewSet):
    queryset = HotelReservation.objects.all()
    serializer_class = HotelReservationSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)