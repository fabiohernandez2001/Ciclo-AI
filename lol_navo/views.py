from rest_framework import viewsets
from rest_framework.response import Response
from .models import Champion
from .serializers import ChampionSerializer

class ChampionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Champion.objects.all().order_by("name")
    serializer_class = ChampionSerializer
    pagination_class = None
#Hay que cambiar esto porque no esta serializado y to eso
    def get_queryset(self):
        queryset = Champion.objects.all().order_by("name")
        name = self.request.query_params.get("name")  # obtiene ?name=Ahri
        if name:
            queryset = queryset.filter(name__icontains=name)  # busca coincidencias parciales
        return queryset