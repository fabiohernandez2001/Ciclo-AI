from rest_framework import serializers
from .models import Champion, Summoner

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = "__all__"
    def create(self, validated_data):
        return Champion.objects.get(**validated_data)
    
class SummonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summoner
        fields = "__all__"
    def create(self, validated_data):
        return Summoner.objects.get(**validated_data)