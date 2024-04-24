from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .movie import Movie

class Review(models.Model):
    full_name = models.CharField(max_length=50)
    #nullable incase the user only wants to leave a rating 
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_created = models.DateField(auto_now_add=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)