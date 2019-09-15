from django.shortcuts import render
from rest_framework import viewsets
from . import models

# Create your views here.
class FoesViewSet(viewsets.ModelViewSet):
    queryset = models.Foe.objects.all()
    serializer_class = models.FoeSerializer

class PlayersViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = models.PlayerSerializer

class EncountersViewSet(viewsets.ModelViewSet):
    queryset = models.Encounter.objects.all()
    serializer_class = models.EncounterSerializer

class EncounterFoesViewSet(viewsets.ModelViewSet):
    queryset = models.EncounterFoe.objects.all()
    serializer_class = models.EncounterFoeSerializer
