from django.db import models
from account.models import User

# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length= 100, unique=True)
    description = models.TextField(max_length= 500, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'media/places', null=True, blank=True, default="")
    top_deal = models.BooleanField(default=False)
    age = models.IntegerField()
    duration = models.CharField(max_length= 30)
    Start_time = models.CharField(max_length= 30)
    
    def __str__(self):
        return self.place_name
class TripTracker(models.Model):
    place = models.ForeignKey(Place, on_delete= models.CASCADE, related_name="triptracker")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.user} place: {self.place}"

    class Meta:
        unique_together = ('place', 'user')
        
class PlacesRating(models.Model):
    places = models.ForeignKey(Place, on_delete= models.CASCADE, related_name="rating")        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=(
                                                    (1,"1 Star"),
                                                    (2,"2 Star"),
                                                    (3,"3 Star"),
                                                    (4,"4 Star"),
                                                    (5,"5 Star") 
                                                  ))
    rating_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('places', 'user')