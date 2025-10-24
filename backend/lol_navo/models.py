from django.db import models
from django.contrib.postgres.fields import ArrayField

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

class Match(models.Model):
     Winner_number = {200, 100}
     id = models.PositiveSmallIntegerField(primary_key=True)
     duration = models.DurationField()
     winner_team = models.PositiveSmallIntegerField(choices=Winner_number)
     time_lane = models.CharField(max_length=100)
     gold_diff = models.PositiveBigIntegerField()
     summoners = models.ManyToManyField(Summoner,
                                        through_fields=('matchid', 'Puuid'),
                                        through='Matchs_Summoners',
                                        related_name='matches')



class Champion(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    Champion_name = models.CharField(max_length=16)
    Champion_Role = models.CharField(max_length=20)
    Champion_description = models.CharField(max_length=255)
    Champion_winrate = models.FloatField()
    Champion_banrate = models.FloatField()
    Champion_pickrate = models.FloatField()
    summoners = models.ManyToManyField(Summoner,
                                         through_fields=('champion_id', 'Puuid'),
                                         through='ChampionStat',
                                         related_name='champions')
class Runes(models.Model):
     id = models.PositiveSmallIntegerField(primary_key=True)
     rune_name = models.CharField(20)
     rune_value = models.PositiveSmallIntegerField()
     rune_description = models.CharField(max_length=200)


class Item(models.Model):
     id = models.PositiveSmallIntegerField(primary_key=True)
     item_name = models.CharField(20)
     item_value = models.PositiveSmallIntegerField()
     item_description = models.CharField(max_length=200)


class Matchs_Summoners(models.Model):
     Win_definition = {'Yes', 'No'}

     match_id = models.PositiveBigIntegerField(primary_key=True)
     Puuid = models.ForeignKey(Summoner, on_delete=models.CASCADE)
     champion_id = models.ForeignKey(Champion, on_delete=models.CASCADE)
     build = ArrayField(models.ForeignKey(Item, on_delete=models.CASCADE))
     runes = ArrayField(models.ForeignKey(Runes, on_delete=models.CASCADE))
     '''build y runes tienen que ser una lista'''
     skill_order = models.CharField(max_length=255)
     cs = models.PositiveIntegerField()
     wards_used = models.PositiveSmallIntegerField()
     vision_points = models.PositiveSmallIntegerField()
     damage_dealt = models.BigIntegerField()
     damage_received = models.BigIntegerField()
     damage_healed = models.BigIntegerField()
     damage_mitigated = models.BigIntegerField()
     game_type = models.CharField(max_length=16)
     winner = models.CharField(choices=Win_definition)
     ranked_points = models.PositiveBigIntegerField()
     kills = models.PositiveSmallIntegerField()
     deaths = models.PositiveIntegerField()
     Assists = models.PositiveIntegerField()
     total_gold = models.PositiveBigIntegerField()
     


    
class ChampionStat(models.Model):
     Puuid = models.ForeignKey(Summoner, on_delete=models.CASCADE)
     champion_id = models.ForeignKey(Champion, on_delete=models.CASCADE)
     champion_point = models.PositiveBigIntegerField()
     champion_winrate = models.FloatField(default=0)   



    
