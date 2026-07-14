from datetime import timedelta

from django.db.models import Prefetch
from django.utils import timezone
from django.db.models import F, FloatField, ExpressionWrapper
from django.db.models.functions import Power
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

    queryset = (
        self.queryset
        .select_related(
            "id_rider",
            "id_driver",
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

    latitude = self.request.query_params.get("latitude")
    longitude = self.request.query_params.get("longitude")

    if latitude and longitude:
        latitude = float(latitude)
        longitude = float(longitude)

        queryset = queryset.annotate(
            distance=ExpressionWrapper(
                Power(F("pickup_latitude") - latitude, 2) +
                Power(F("pickup_longitude") - longitude, 2),
                output_field=FloatField(),
            )
        ).order_by("distance")

    return queryset



class RideEventViewSet(viewsets.ModelViewSet):

    queryset = RideEvent.objects.all()

    serializer_class = RideEventSerializer

    #permission_classes = [IsAdminRole]