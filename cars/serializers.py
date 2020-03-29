from rest_framework import serializers

from cars.models import Car


class CarDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin', 'id', 'user',)
