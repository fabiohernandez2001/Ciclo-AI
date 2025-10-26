from rest_framework import viewsets

from .models import Champion
from .serializers import ChampionSerializer


class ChampionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Champion.objects.all().order_by("champion_name")
    serializer_class = ChampionSerializer
    pagination_class = None
