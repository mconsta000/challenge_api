from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
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

class PartiesViewSet(viewsets.ModelViewSet):
    queryset = models.Party.objects.all()
    serializer_class = models.PartySerializer

    @action(detail=True, methods=['get'])
    def encounter(self, request, *args, **kwargs):
        party = self.get_object()
        party_serializer = self.get_serializer(party)

        encounter_id = int(kwargs['encounter_id'])
        encounter = models.Encounter.objects.get(pk=encounter_id)
        encounter_serializer = models.EncounterSerializer(encounter, context={'request': request})

        encounters = []
        encounters.append(encounter_serializer.data)

        response = party_serializer.data
        response["encounters"] = encounters

        return Response({"party": response})
