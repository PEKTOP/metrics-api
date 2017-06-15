from rest_framework.serializers import Serializer, ModelSerializer, ValidationError

from .models import Activity, Location, Sleep


class BaseSerializer(Serializer):
    """
    Base Serializer
    """

    def validate(self, data):
        if data['time_start'] >= data['time_end']:
            raise ValidationError('Start date should be prior to end date')
        return data

    class Meta:
        fields = (
            'id',
            'time_start',
            'time_end',
        )


class ActivitySerializer(BaseSerializer, ModelSerializer):
    """
    Activity Serializer
    """
    class Meta:
        model = Activity
        fields = BaseSerializer.Meta.fields + (
            'value',
        )

class LocationSerializer(ModelSerializer):
    """
    Location Serializer
    """
    class Meta:
        model = Location
        fields = BaseSerializer.Meta.fields + (
            'latitude',
            'longitude',
        )

class SleepSerializer(ModelSerializer):
    """
    Sleep Serializer
    """
    class Meta:
        model = Sleep
        fields = BaseSerializer.Meta.fields
