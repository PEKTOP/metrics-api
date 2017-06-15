from rest_framework.viewsets import ModelViewSet

from .filters import ActivityFilter, LocationFilter, SleepFilter
from .models import Activity, Location, Sleep
from .serializers import ActivitySerializer, LocationSerializer, SleepSerializer


class ActivityViewSet(ModelViewSet):
    """
    Activity endpoint
    """
    filter_class = ActivityFilter
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LocationViewSet(ModelViewSet):
    """
    Location endpoint
    """
    filter_class = LocationFilter
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SleepViewSet(ModelViewSet):
    """
    Sleep endpoint
    """
    filter_class = SleepFilter
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
