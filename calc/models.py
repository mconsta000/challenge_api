from django.db import models
from rest_framework import serializers

class Foe(models.Model):
    name = models.CharField(max_length=50)
    xp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foe
        fields = ['url','name','xp']

class Player(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url','name','level']

class Party(models.Model):
    name = models.CharField(max_length=50)
    member = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Party
            fields = ['url','name','member']

class FoeEncounters(models.Model):
    foe = models.ForeignKey(Foe, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.foe.name + " " + str(self.count)

class FoeEncountersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoeEncounters
        fields = ['url', 'foe', 'count']

class Encounter(models.Model):
    name = models.CharField(max_length=50)
    foes = models.ManyToManyField(FoeEncounters)

    def __str__(self):
        return self.name

class EncounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encounter
        fields = ['url', 'name', 'foes']