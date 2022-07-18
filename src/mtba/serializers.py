import requests

from .models import Routes, Stops, DirectionDestination
from rest_framework import serializers


class DirectionDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionDestination
        fields = ["name"]


class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ["name", "route_id", "fare_class", "direction_destinations"]

    @staticmethod
    def get(url, *args, **kwargs) -> dict:
        """
        Get response from mtba endpoint, updates database and returns a response.

        :param str url: the url for the mtba endpoint.

        :return dict { message, url, status_code }
        """

        response = requests.get(url, stream=False, timeout=10)

        if response.status_code == 200:
            response_data = response.json().pop("data", None)

            for record in response_data:
                serializer = RoutesSerializer(data=record)
                if serializer.is_valid(raise_exception=True):
                    attributes = record.get("attributes", None)
                    direction_destinations = attributes.get(
                        "direction_destinations", None
                    )
                    record.pop("attributes")
                    route, created = Routes.objects.update_or_create(**record)

                    for destination in direction_destinations:
                        destination_object, created = DirectionDestination.objects.get_or_create(
                            name=destination
                        )
                        route.direction_destinations.add(
                            DirectionDestination.objects.get(name=destination)
                        )

            return {
                "message": "success",
                "url": url,
                "status_code": response.status_code,
            }
        else:
            return {
                "message": f"Invalid http status code from: {url}",
                "url": url,
                "status_code": response.status_code,
            }

    def to_internal_value(self, data):
        route_id = data.pop("id")
        attributes = data.get("attributes")
        data.update(
            {
                "route_id": str(route_id),
                "fare_class": str(attributes.get("fare_class", None)),
                "name": str(attributes.get("long_name", None)),
            }
        )
        data.pop("links")
        data.pop("relationships")
        data.pop("type")
        return super().to_internal_value(data)


class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = ["stop_id", "platform_name", "description"]

    @staticmethod
    def get(url, *args, **kwargs) -> dict:
        """
        Get response from mtba endpoint, updates database and returns a response.

        :param str url: the url for the mtba endpoint.

        :return dict { message, url, status_code }
        """

        result = []
        response = requests.get(url, stream=False, timeout=10)

        if response.status_code == 200:
            response_data = response.json().pop("data", None)

            for record in response_data:
                serializer = StopsSerializer(data=record)
                if serializer.is_valid(raise_exception=True):
                    stop, created = Stops.objects.update_or_create(**record)
                    result.append(stop)

            return {
                "message": "success",
                "url": url,
                "status_code": response.status_code,
            }
        else:
            return {
                "message": f"Invalid http status code from: {url}",
                "url": url,
                "status_code": response.status_code,
            }

    def to_internal_value(self, data):
        stop_id = data.pop("id")
        attributes = data.pop("attributes")
        description = attributes.get("description", None)
        if description:
            description = (
                (description[:255] + "..") if len(description) > 255 else description
            )
        data.update(
            {
                "stop_id": str(stop_id),
                "platform_name": str(attributes.get("platform_name", None)),
                "description": str(description),
            }
        )
        data.pop("links")
        data.pop("relationships")
        data.pop("type")
        return super().to_internal_value(data)
