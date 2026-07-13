from django.contrib import admin

from .models import User
from .models import Ride
from .models import RideEvent


admin.site.register(User)
admin.site.register(Ride)
admin.site.register(RideEvent)
