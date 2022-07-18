from rest_framework.views import APIView
from .models import Routes, DirectionDestination
from rest_framework import status
from .serializers import RoutesSerializer, StopsSerializer
from django.http import JsonResponse


class RoutesView(APIView):
    serializer = RoutesSerializer

    def get(self, request, *args, **kwargs):
        routes_url = "https://api-v3.mbta.com/routes"
        routes_data = self.serializer.get(routes_url)
        if routes_data.get("status_code", None) != status.HTTP_200_OK:
            return JsonResponse(
                {
                    "message": routes_data.get("message", None),
                    "url": routes_data.get("url", None),
                    "status_code": routes_data.get("status_code", None),
                    "queryset": None,
                }
            )

        queryset = Routes.objects.all().values()
        return JsonResponse(
            {
                "message": routes_data.get("message", None),
                "url": routes_data.get("url", None),
                "status_code": routes_data.get("status_code", None),
                "queryset": list(queryset),
            }
        )


class StopsView(APIView):
    serializer = StopsSerializer

    def get(self, request, *args, **kwargs):

        routes_url = "https://api-v3.mbta.com/routes"
        stops_url = "https://api-v3.mbta.com/stops"

        routes_data = RoutesSerializer.get(url=routes_url)
        route_id = kwargs.get("route_id", None)

        if not route_id:
            route_id = self.request.GET.get("route_id", None)

        if routes_data.get("status_code", None) != status.HTTP_200_OK:
            return JsonResponse(
                {
                    "message": routes_data.get("message", None),
                    "url": routes_data.get("url", None),
                    "status_code": routes_data.get("status_code", None),
                    "queryset": None,
                }
            )

        stops_data = self.serializer.get(url=stops_url)

        if route_id:
            route = Routes.objects.get(route_id=str(route_id))
            if not route:
                return JsonResponse(
                    {
                        "message": f"{route_id} was not found.",
                        "url": stops_url,
                        "status_code": stops_data.get("status_code", None),
                        "queryset": None,
                    }
                )
            queryset = route.direction_destinations.all().values()
        else:
            queryset = DirectionDestination.objects.all().values()

        return JsonResponse(
            {
                "message": stops_data.get("message", None),
                "url": stops_data.get("url", None),
                "status_code": stops_data.get("status_code", None),
                "queryset": list(queryset),
            }
        )
