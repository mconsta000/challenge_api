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

class Encounter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EncounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encounter
        fields = ['url','name']

class EncounterFoe(models.Model):
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    foe = models.ForeignKey(Foe, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.foe 

class EncounterFoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EncounterFoe
        fields = ['url','encounter','foe', 'count']
