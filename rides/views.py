from datetime import timedelta
from rest_framework.exceptions import ValidationError
from django.db.models import (
    Prefetch,
    F,
    FloatField,
    ExpressionWrapper,
    Value,
)
from django.db.models.functions import Power
from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import User, Ride, RideEvent
from .serializers import (
    UserSerializer,
    RideSerializer,
    RideEventSerializer,
)
from .permissions import IsAdminRole
from .filters import RideFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminRole]


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    # permission_classes = [IsAdminRole]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_class = RideFilter

    search_fields = [
        "id_rider__first_name",
        "id_rider__last_name",
        "id_rider__email",
        "id_driver__first_name",
        "id_driver__last_name",
        "id_driver__email",
    ]

    ordering_fields = [
        "pickup_time",
    ]

    ordering = [
        "-pickup_time",
    ]

    def get_queryset(self):
        yesterday = timezone.now() - timedelta(hours=24)

        queryset = (
            Ride.objects.select_related(
                "id_rider",
                "id_driver",
            ).prefetch_related(
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

        print("Latitude:", latitude)
        print("Longitude:", longitude)

        # If only one coordinate is supplied
        if (latitude and not longitude) or (longitude and not latitude):
            raise ValidationError(
                {
                    "detail": (
                        "Both latitude and longitude must be provided "
                        "to sort rides by distance."
                    )
                }
            )

        # Distance sorting
        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except (TypeError, ValueError):
                raise ValidationError(
                    {
                        "detail": (
                            "Latitude and longitude must be valid numbers."
                        )
                    }
                )

            print("Distance sorting activated")

            queryset = queryset.annotate(
                distance=ExpressionWrapper(
                    (
                        (F("pickup_latitude") - Value(latitude))
                        * (F("pickup_latitude") - Value(latitude))
                    )
                    + (
                        (F("pickup_longitude") - Value(longitude))
                        * (F("pickup_longitude") - Value(longitude))
                    ),
                    output_field=FloatField(),
                )
            ).order_by("distance")

        return queryset


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    # permission_classes = [IsAdminRole]