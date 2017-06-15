from django.conf.urls import url

from .views import ActivityViewSet, LocationViewSet, SleepViewSet

urlpatterns = [
    url(
        regex=r'^activity$',
        view=ActivityViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='activity-list',
    ),
    url(
        regex=r'^activity/(?P<pk>[0-9]+)$',
        view=ActivityViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }),
        name='activity-detail',
    ),
    url(
        regex=r'^locations$',
        view=LocationViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='location-list',
    ),
    url(
        regex=r'^locations/(?P<pk>[0-9]+)$',
        view=LocationViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }),
        name='location-detail',
    ),
    url(
        regex=r'^sleep$',
        view=SleepViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='sleep-list',
    ),
    url(
        regex=r'^sleep/(?P<pk>[0-9]+)$',
        view=SleepViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }),
        name='sleep-detail',
    ),
]
