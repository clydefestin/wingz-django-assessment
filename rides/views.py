from datetime import timedelta

from django.db.models import Prefetch
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .filters import RideFilter
from .models import User, Ride, RideEvent
from .permissions import IsAdminRole
from .serializers import (
    UserSerializer,
    RideSerializer,
    RideEventSerializer,
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    #permission_classes = [IsAdminRole]


class RideViewSet(viewsets.ModelViewSet):

    queryset = Ride.objects.all()

    serializer_class = RideSerializer

    #permission_classes = [IsAdminRole]

    filterset_class = RideFilter

     # Search
    search_fields = [
        "id_rider__first_name",
        "id_rider__last_name",
        "id_rider__email",
        "id_driver__first_name",
        "id_driver__last_name",
        "id_driver__email",
    ]

    ordering_fields = ["pickup_time"]

    def get_queryset(self):

        yesterday = timezone.now() - timedelta(hours=24)

        return (
           self.queryset
           .select_related(
                "id_driver",
                "id_rider",
            )
           .prefetch_related(
               Prefetch(
                   "ride_events",
                   queryset=RideEvent.objects.filter(
                       created_at__gte=yesterday
                   ),
               )
           )
       )




class RideEventViewSet(viewsets.ModelViewSet):

    queryset = RideEvent.objects.all()

    serializer_class = RideEventSerializer

    #permission_classes = [IsAdminRole]