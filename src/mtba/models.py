from django.db import models


class DirectionDestination(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Routes(models.Model):
    """
    Expected object shape from mtba endpoint:
    {
       "attributes":{
          "color":"DA291C",
          "description":"Rapid Transit",
          "direction_destinations":[
             "Ashmont/Braintree",
             "Alewife"
          ],
          "direction_names":[
             "South",
             "North"
          ],
          "fare_class":"Rapid Transit",
          "long_name":"Red Line",
          "short_name":"",
          "sort_order":10010,
          "text_color":"FFFFFF",
          "type":1
       },
       "id":"Red",
       "links":{
          "self":"/routes/Red"
       },
       "relationships":{
          "line":{
             "data":{
                "id":"line-Red",
                "type":"line"
             }
          }
       },
       "type":"route"
    }
    """

    name = models.CharField(max_length=100, default=None)
    route_id = models.CharField(max_length=100, default=None)
    fare_class = models.CharField(max_length=100, default=None)
    direction_destinations = models.ManyToManyField(DirectionDestination, null=True)

    # <QuerySet [<DirectionDestination: Ashmont/Braintree>, <DirectionDestination: Alewife>]>

    def __str__(self):
        return self.name


class Stops(models.Model):
    """
    Expected object shape from mtba endpoint:
    {
       "attributes":{
          "address":"None",
          "at_street":"None",
          "description":"None",
          "latitude":42.135099,
          "location_type":0,
          "longitude":-71.039942,
          "municipality":"Avon",
          "name":"47 N Main St",
          "on_street":"North Main Street",
          "platform_code":"None",
          "platform_name":"None",
          "vehicle_type":3,
          "wheelchair_boarding":1
       },
       "id":"4230",
       "links":{
          "self":"/stops/4230"
       },
       "relationships":{
          "facilities":{
             "links":{
                "related":"/facilities/?filter[stop]=4230"
             }
          },
          "parent_station":{
             "data":"None"
          },
          "zone":{
             "data":{
                "id":"LocalBus",
                "type":"zone"
             }
          }
       },
       "type":"stop"
    }
    """

    stop_id = models.CharField(max_length=100, null=True)
    platform_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.platform_name
