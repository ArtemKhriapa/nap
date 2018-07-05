from rest_framework import serializers
from ..models import Data as Data_model

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data_model
        fields = (
            'id',
            'text',
            'user',
        )
