from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    RideViewSet,
    RideEventViewSet,
)

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("rides", RideViewSet)
router.register("ride-events", RideEventViewSet)

urlpatterns = router.urls