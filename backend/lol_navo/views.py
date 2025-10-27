from rest_framework import viewsets
from rest_framework.response import Response

from .models import Champion
from .serializers import ChampionSerializer


class ChampionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Champion.objects.all().order_by("champion_name")
    serializer_class = ChampionSerializer
    pagination_class = None
    def get(self, request):
        champion = Champion.objects.get(self.request.query_params.get("name"))
        champion_serializer = ChampionSerializer(champion)
        return Response(champion_serializer.data)
       