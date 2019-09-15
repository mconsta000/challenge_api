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

class FoeEncountersViewSet(viewsets.ModelViewSet):
    queryset = models.FoeEncounters.objects.all()
    serializer_class = models.FoeEncountersSerializer
