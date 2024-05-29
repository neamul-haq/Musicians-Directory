from django.db import models

# Create your models here.
class Musician(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=13)
    instrumentType = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.firstName + self.lastName