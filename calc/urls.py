from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'foes', views.FoesViewSet)
router.register(r'players', views.PlayersViewSet)
router.register(r'encounters', views.EncountersViewSet)
router.register(r'foe-encounters', views.FoeEncountersViewSet)
router.register(r'parties', views.PartiesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]