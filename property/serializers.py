from rest_framework.serializers import ModelSerializer
from .models import Property


class PropertySerializer(ModelSerializer):

    class Meta:
        model = Property

        fields = ['property_auto', 'property_block', 'property_name', 'property_type', 'property_category',
                  'property_year'
                  ]
