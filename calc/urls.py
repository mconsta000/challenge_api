from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'foes', views.FoesViewSet)
router.register(r'players', views.PlayersViewSet)
router.register(r'encounters', views.EncountersViewSet)
router.register(r'encounterfoes', views.EncounterFoesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]