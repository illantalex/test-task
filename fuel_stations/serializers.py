from rest_framework import serializers

from .models import GasStationCompany, GasStation

# Create your serializers here
class GasStationCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = GasStationCompany
        fields = ('id', 'name', 'address')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = ('id', 'name', 'address', 'latitude', 'longitude', 'company')

    def validate(self, attrs):
        if not attrs['company'] in self.context['request'].user.gas_station_companies.all():
            raise serializers.ValidationError("You are not allowed to create stations for this company")
        return super().validate(attrs)


class GasStationCompanyDetailSerializer(serializers.ModelSerializer):
    gas_stations = GasStationSerializer(many=True, read_only=True)

    class Meta:
        model = GasStationCompany
        fields = ('id', 'name', 'address', 'gas_stations')
