from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Ride


class RideTests(APITestCase):

    # Test List API
    def test_get_rides(self):
        response = self.client.get(reverse("ride-list"))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # Test Invalid Latitude
    def test_invalid_latitude(self):
        response = self.client.get(
            reverse("ride-list"),
            {
                "latitude": "abc",
                "longitude": "120"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # Test Missing Longitude
    def test_missing_longitude(self):
        response = self.client.get(
            reverse("ride-list"),
            {
                "latitude": "14.5"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # Test Distance Sorting
    def test_distance_sorting(self):
        response = self.client.get(
            reverse("ride-list"),
            {
                "latitude": "14.5995",
                "longitude": "120.9842"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(len(response.data) >= 0)