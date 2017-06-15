from django_filters import FilterSet, IsoDateTimeFilter

from .models import Activity, Location, Sleep


class BaseMetricFilter(FilterSet):
    """
    Base Metric Filter
    """
    time_start = IsoDateTimeFilter(name='time_start', lookup_expr='gte')
    time_end = IsoDateTimeFilter(name='time_start', lookup_expr='lt')

    class Meta:
        fields = (
            'time_start',
            'time_end',
        )


class ActivityFilter(BaseMetricFilter):
    """
    Activity Filter
    """
    class Meta(BaseMetricFilter.Meta):
        model = Activity


class LocationFilter(BaseMetricFilter):
    """
    Location Filter
    """
    class Meta(BaseMetricFilter.Meta):
        model = Location


class SleepFilter(BaseMetricFilter):
    """
    Sleep Filter
    """
    class Meta(BaseMetricFilter.Meta):
        model = Sleep
