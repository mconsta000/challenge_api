from challenge.calc import XPThresholdCalc
from challenge.calc import EncounterXPCalc
from challenge.calc import EncounterDifficultyCalc

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
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

    def encounter(self, request, *args, **kwargs):
        calc_party = XPThresholdCalc()
        calc_encounter = EncounterXPCalc()
        calc_difficulty = EncounterDifficultyCalc(calc_encounter, calc_party)

        party = self.get_object()
        party_serializer = self.get_serializer(party)

        # Set up the party level calculation
        for player in party.player.all():
            calc_party.add_party_level(player.level)

        encounter_id = int(kwargs['encounter_id'])
        encounter = models.Encounter.objects.get(pk=encounter_id)

        # Iterate through each encounter and calculate challenge
        for f in encounter.foes.all():
            calc_encounter.add_encounter_xp(f.foe.xp * f.count)

        encounter.challenge = calc_difficulty.calculate_difficulty()
        calc_encounter.reset()

        # Serialize the encounters 
        encounter_serializer = models.EncounterSerializer(encounter, context={'request': request})

        encounters_serialized = [encounter_serializer.data]

        response = party_serializer.data
        response["encounters"] = encounters_serialized

        return Response({"party": response})

    @action(detail=True, methods=['get'])
    def encounters(self, request, *args, **kwargs):
        calc_party = XPThresholdCalc()
        calc_encounter = EncounterXPCalc()
        calc_difficulty = EncounterDifficultyCalc(calc_encounter, calc_party)

        party = self.get_object()
        party_serializer = self.get_serializer(party)

        # Set up the party level calculation
        for player in party.player.all():
            calc_party.add_party_level(player.level)

        # Iterate through each encounter and calculate challenge
        encounters = models.Encounter.objects.all()
        for encounter in encounters:
            for f in encounter.foes.all():
                calc_encounter.add_encounter_xp(f.foe.xp * f.count)
            
            encounter.challenge = calc_difficulty.calculate_difficulty()
            calc_encounter.reset()
            
        # Serialize the encounters 
        encounter_serializer = models.EncounterSerializer(encounters, many=True, context={'request': request})

        encounters_serialized = []
        encounters_serialized.extend(encounter_serializer.data)

        # Add the calculated encounters to the party data
        response = party_serializer.data
        response["encounters"] = encounters_serialized

        return Response({"party": response})
