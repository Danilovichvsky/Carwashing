import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarWashing.settings")
django.setup()
from rest_framework.response import Response
from rest_framework.views import APIView

BD = [{"name": "danya", "secondname": "bulya", "age": 22},
      {"name": "danya2", "secondname": "bulya2", "age": 2222}]

class BulSerializer:
    def __init__(self, instance):
        self.instance = instance

    def to_represent(self):
        return {
            "name": self.instance.get("name", ""),
            "secondname": self.instance.get("secondname", ""),
            "age": self.instance.get("age", 0)
        }

    @property
    def data(self):
        # Call to_represent only when data is accessed
        return self.to_represent()

class BulyaViewSet(APIView):
    serializer_class = BulSerializer
    """
    A simple ViewSet for listing or retrieving users.
    """
    def get(self, request):
        serialized_data = [BulSerializer(item).data for item in BD]  # List comprehension for serialization
        return Response({"data": serialized_data})