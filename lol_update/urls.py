from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
'''
from .views import ChampionViewSet


app_name = "lol_navo"

router = DefaultRouter()
router.register(r'champions', ChampionViewSet, basename="champion")

urlpatterns = router.urls
'''
urlpatterns = [path("champions", views.get_champions, name="champions"),
               path("items", views.get_items, name="items"),]