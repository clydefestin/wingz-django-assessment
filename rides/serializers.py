from rest_framework import serializers

from .models import User
from .models import Ride
from .models import RideEvent

#UserSerializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

#RideEventSerializer
class RideEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideEvent
        fields = "__all__"


#RideSerializer
class RideSerializer(serializers.ModelSerializer):

    rider = UserSerializer(source="id_rider", read_only=True)

    driver = UserSerializer(source="id_driver", read_only=True)

    ride_events = RideEventSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Ride
        fields = "__all__"