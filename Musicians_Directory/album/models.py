from django.db import models
from django.db.models import SET_NULL
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    album_release_date = models.DateTimeField(auto_now_add=True)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    
    def __str__(self) -> str:
        return self.album_name