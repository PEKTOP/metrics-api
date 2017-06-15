from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Activity

class ActivityTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Activity.objects.create(
            time_start='2017-06-15T10:00:00Z',
            time_end='2017-06-15T11:00:00Z',
            value=3600,
        )

    def test_create_activity(self):
        response = self.client.post(reverse('metrics:activity-list'), {
            'time_start': '2017-06-15T11:00:00Z',
            'time_end': '2017-06-15T12:00:00Z',
            'value': 7200
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_activity(self):
        response = self.client.get(reverse('metrics:activity-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_activity(self):
        response = self.client.get(reverse('metrics:activity-detail', kwargs={'pk': 1}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_activity(self):
        response = self.client.put(reverse('metrics:activity-detail', kwargs={'pk': 1}), {
            'time_start': '2017-06-15T10:00:00Z',
            'time_end': '2017-06-15T11:00:00Z',
            'value': 7200,
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_activity(self):
        response = self.client.delete(reverse('metrics:activity-detail', kwargs={'pk': 1}),
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

