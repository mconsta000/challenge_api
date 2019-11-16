from django.db import models
from rest_framework import serializers

class Foe(models.Model):
    name = models.CharField(max_length=50)
    xp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foe
        fields = ['id','url','name','xp']

class Player(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','url','name','level']

class Party(models.Model):
    name = models.CharField(max_length=50)
    player = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

class PartySerializer(serializers.ModelSerializer):
    class Meta:
            model = Party
            fields = ['id','url','name','player']

class FoeEncounters(models.Model):
    foe = models.ForeignKey(Foe, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.foe.name + " " + str(self.count)

class FoeEncountersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoeEncounters
        fields = ['id','url', 'foe', 'count']

class Encounter(models.Model):
    name = models.CharField(max_length=50)
    foes = models.ManyToManyField(FoeEncounters)
    challenge = ''

    def __str__(self):
        return self.name

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = ['id','url', 'name', 'foes', 'challenge']