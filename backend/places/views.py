from .models import Place, PlacesRating,TripTracker
from .serializers import PlacesSerializer, PlacesRatingSerializer, TripTrackerSerializer
from rest_framework import viewsets

class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlacesSerializer

class PlacesRatingViewSet(viewsets.ModelViewSet):
    queryset = PlacesRating.objects.all()
    serializer_class = PlacesRatingSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TripTrackerViewSet(viewsets.ModelViewSet):
    queryset = TripTracker.objects.all()
    serializer_class = TripTrackerSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)