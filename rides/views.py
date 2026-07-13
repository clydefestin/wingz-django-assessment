from rest_framework import viewsets

from .models import User
from .models import Ride
from .models import RideEvent

from .serializers import (
    UserSerializer,
    RideSerializer,
    RideEventSerializer,
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer

class RideViewSet(viewsets.ModelViewSet):

    queryset = Ride.objects.all()

    serializer_class = RideSerializer

class RideEventViewSet(viewsets.ModelViewSet):

    queryset = RideEvent.objects.all()

    serializer_class = RideEventSerializer
