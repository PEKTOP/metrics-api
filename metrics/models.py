from django.db import models


class MetricAbstractModel(models.Model):
    """
    Metric Abstract Model
    """
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    class Meta:
        abstract = True

class Activity(MetricAbstractModel):
    """
    Activity by foot
    """
    value = models.PositiveIntegerField()


class Location(MetricAbstractModel):
    """
    Point on the map
    """
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)


class Sleep(MetricAbstractModel):
    """
    Sleep period
    """
    pass
