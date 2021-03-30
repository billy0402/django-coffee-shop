from rest_framework.viewsets import ModelViewSet

from api.serializers import CoffeeSerializer
from coffees.models import Coffee


# Create your views here.
class CoffeeViewSet(ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
