from rest_framework import serializers

from .models import User
from .models import Ride
from .models import RideEvent

#UserSerializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
        ]

#RideEventSerializer
class RideEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideEvent
        fields = [
            "id_ride_event",
            "description",
            "created_at",
        ]


#RideSerializer
class RideSerializer(serializers.ModelSerializer):

    distance = serializers.FloatField(read_only=True)

    rider = UserSerializer(
        source="id_rider",
        read_only=True,
    )

    driver = UserSerializer(
        source="id_driver",
        read_only=True,
    )

    todays_ride_events = RideEventSerializer(
        source="ride_events",
        many=True,
        read_only=True,
    )


    class Meta:
        model = Ride

        fields = [
            "id_ride",
            "status",
            "pickup_latitude",
            "pickup_longitude",
            "dropoff_latitude",
            "dropoff_longitude",
            "pickup_time",
            "distance",
            "id_rider",
            "id_driver",
            "rider",
            "driver",
            "todays_ride_events",
        ]