from rest_framework.routers import DefaultRouter

from .views import ChampionViewSet


app_name = "lol_navo"

router = DefaultRouter()
router.register("champions", ChampionViewSet, basename="champion")

urlpatterns = router.urls
