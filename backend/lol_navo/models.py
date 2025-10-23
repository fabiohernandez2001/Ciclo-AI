from django.db import models

class Summoner(models.Model):
     Puuid = models.CharField(primary_key=True, max_length=72)
     Username = models.CharField(max_length=16)
     Server = models.CharField(max_length=5)
     Icon = models.URLField()
     Ranked_solo_rank = models.CharField(max_length=32, default="Unranked")
     Ranked_flex_rank = models.CharField(max_length=32, default="Unranked")
     Ranked_solo_wins = models. PositiveSmallIntegerField()
     Ranked_solo_loses = models. PositiveSmallIntegerField()
     Ranked_flex_wins = models. PositiveSmallIntegerField()
     Ranked_flex_loses = models. PositiveSmallIntegerField()
     Quickplay_wins = models. PositiveSmallIntegerField()
     Quickplay_loses = models. PositiveSmallIntegerField()
     Normal_wins = models. PositiveSmallIntegerField()
     Normal_loses = models. PositiveSmallIntegerField()
     Aram_wins = models. PositiveSmallIntegerField()
     Aram_loses = models. PositiveSmallIntegerField()
     Arena_wins = models. PositiveSmallIntegerField()
     Arena_loses = models. PositiveSmallIntegerField()
     Clash_wins = models. PositiveSmallIntegerField()
     Clash_loses = models. PositiveSmallIntegerField()
#class Item(models.Model):



#class Champion(models.Model):
    

    
