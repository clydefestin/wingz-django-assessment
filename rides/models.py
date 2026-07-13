from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, default="user")
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


#Ride Model
class Ride(models.Model):
    STATUS_CHOICES = [
        ("en-route", "En Route"),
        ("pickup", "Pickup"),
        ("dropoff", "Dropoff"),
    ]

    id_ride = models.AutoField(primary_key=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    id_rider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rides_as_rider"
    )

    id_driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rides_as_driver"
    )

    pickup_latitude = models.FloatField()

    pickup_longitude = models.FloatField()

    dropoff_latitude = models.FloatField()

    dropoff_longitude = models.FloatField()

    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"Ride {self.id_ride}"

#RideEvent Model
class RideEvent(models.Model):

    id_ride_event = models.AutoField(primary_key=True)

    id_ride = models.ForeignKey(
        Ride,
        on_delete=models.CASCADE,
        related_name="ride_events"
    )

    description = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
