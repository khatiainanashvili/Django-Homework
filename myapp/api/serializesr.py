from rest_framework.serializers import ModelSerializer

from ..models import Birds


class BirdSerializer(ModelSerializer):
    class Meta:
        model = Birds
        fields = '__all__'