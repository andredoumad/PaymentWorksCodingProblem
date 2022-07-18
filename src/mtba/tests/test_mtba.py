import pytest
import requests
from django.urls import reverse

from ..serializers import RoutesSerializer, StopsSerializer
from ..models import Routes, DirectionDestination


class TestMtba:
    @pytest.mark.django_db
    def test_get_routes(self):
        """Makes a few assertions to prove that the data is populated for Routes and destinations"""
        result = RoutesSerializer.get("https://api-v3.mbta.com/routes/")
        assert result is not None
        red_route = Routes.objects.get(route_id="Red")
        assert red_route is not None
        assert red_route.route_id == "Red"
        destinations_for_red_line = red_route.direction_destinations.all()
        all_destinations = DirectionDestination.objects.all()
        assert (
            red_route.direction_destinations.get(name="Ashmont/Braintree") is not None
        )

    @pytest.mark.django_db
    def test_get_stops(self, api_client):
        """Makes a few assertions to prove that the data is populated for Stops"""
        result = api_client.get(f"http://0.0.0.0:8000/mtba/stops/Red")
        assert result is not None
        queryset = result.json().get("queryset", None)
        assert queryset is not None
        assert queryset[0].get("name", None) == "Ashmont/Braintree"
        assert queryset[1].get("name", None) == "Alewife"
