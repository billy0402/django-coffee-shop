from rest_framework.serializers import ModelSerializer

from coffees.models import Coffee


class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'
