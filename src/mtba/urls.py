from django.urls import path, re_path
from .views import RoutesView, StopsView

app_name = "mtba"

urlpatterns = [
    path("", RoutesView.as_view(), name="mtba-home"),
    path("routes/", RoutesView.as_view(), name="mtba-routes"),
    path("stops/", StopsView.as_view(), name="mtba-stops"),
    re_path(r"^stops/(?P<route_id>[\w ]+)/?$", StopsView.as_view(), name="mtba-stops-id"),
]
