from django.db import models
from django.contrib.postgres.fields import ArrayField

class Summoner(models.Model):
     puuid = models.CharField(primary_key=True, max_length=72)
     username = models.CharField(max_length=16)
     server = models.CharField(max_length=5)
     icon = models.URLField()
     
     ranked_solo_rank = models.CharField(max_length=32, default="Unranked")
     ranked_flex_rank = models.CharField(max_length=32, default="Unranked")
     
     ranked_solo_wins = models.PositiveSmallIntegerField(default=0)
     ranked_solo_loses = models.PositiveSmallIntegerField(default=0)
     ranked_flex_wins = models.PositiveSmallIntegerField(default=0)
     ranked_flex_loses = models.PositiveSmallIntegerField(default=0)
     
     quickplay_wins = models.PositiveSmallIntegerField(default=0)
     quickplay_loses = models.PositiveSmallIntegerField(default=0)
     
     normal_wins = models.PositiveSmallIntegerField(default=0)
     normal_loses = models.PositiveSmallIntegerField(default=0)
     
     aram_wins = models.PositiveSmallIntegerField(default=0)
     aram_loses = models.PositiveSmallIntegerField(default=0)
     
     arena_wins = models.PositiveSmallIntegerField(default=0)
     arena_loses = models.PositiveSmallIntegerField(default=0)
     
     clash_wins = models.PositiveSmallIntegerField(default=0)
     clash_loses = models.PositiveSmallIntegerField(default=0)

class Match(models.Model):
     WINNER_CHOICES = ((100, "Blue"), (200, "Red"))
     id = models.BigAutoField(primary_key=True)
     duration = models.DurationField()
     winner_team = models.PositiveSmallIntegerField(choices=WINNER_CHOICES)
     time_lane = models.CharField(max_length=100)
     gold_diff = models.PositiveBigIntegerField()
     summoners = models.ManyToManyField(
          Summoner,
          through_fields=('match', 'summoner'),
          through='MatchSummoners',
          related_name='matches'
     )



class Champion(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    champion_name = models.CharField(max_length=16)
    champion_role = models.CharField(max_length=20)
    champion_description = models.CharField(max_length=255)
    champion_winrate = models.FloatField()
    champion_banrate = models.FloatField()
    champion_pickrate = models.FloatField()
    summoners = models.ManyToManyField(
         Summoner,
          through_fields=('champion', 'summoner'),
          through='ChampionStat',
          related_name='champions'
     )
class Rune(models.Model):
     id = models.PositiveSmallIntegerField(primary_key=True)
     rune_name = models.CharField(max_length=20)
     rune_value = models.PositiveSmallIntegerField()
     rune_description = models.CharField(max_length=200)


class Item(models.Model):
     id = models.PositiveSmallIntegerField(primary_key=True)
     item_name = models.CharField(max_length=20)
     item_value = models.PositiveSmallIntegerField()
     item_description = models.CharField(max_length=200)


class MatchSummoners(models.Model):
     match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="participants")
     summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE, related_name="participations")
     champion = models.ForeignKey(Champion, on_delete=models.SET_NULL, null=True, blank=True)
     #build = ArrayField(models.ForeignKey(Item, on_delete=models.CASCADE))
     #rune = ArrayField(models.ForeignKey(Runes, on_delete=models.CASCADE))
     '''build y runes tienen que ser una lista, posiblemente sea necesario crear tablas intermedias'''
     skill_order = models.CharField(max_length=255, blank=True, default='')
     cs = models.PositiveIntegerField(default=0)
     wards_used = models.PositiveSmallIntegerField(default=0)
     vision_points = models.PositiveSmallIntegerField(default=0)
     damage_dealt = models.BigIntegerField(default=0)
     damage_received = models.BigIntegerField(default=0)
     damage_healed = models.BigIntegerField(default=0)
     damage_mitigated = models.BigIntegerField(default=0)
     game_type = models.CharField(max_length=16)
     winner = models.BooleanField(default=False)
     ranked_points = models.PositiveBigIntegerField(default=0)
     kills = models.PositiveSmallIntegerField(default=0)
     deaths = models.PositiveIntegerField(default=0)
     assists = models.PositiveIntegerField(default=0)
     total_gold = models.PositiveBigIntegerField(default=0)
     
     class Meta:
        constraints = [
            models.UniqueConstraint(fields=["match", "summoner"], name="uniq_match_summoner")
        ]
        indexes = [
            models.Index(fields=["match"]),
            models.Index(fields=["summoner"]),
            models.Index(fields=["match", "summoner"]),
        ]
    
class ChampionStat(models.Model):
     summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE, related_name="champion_stats")
     champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name="summoner_stats")
     champion_point = models.PositiveBigIntegerField(default=0)
     champion_winrate = models.FloatField(default=0.0)   
     champion_kda = models.FloatField(default=0.0)
     champion_games = models.PositiveIntegerField(default=0)

     class Meta:
        constraints = [
            models.UniqueConstraint(fields=["summoner", "champion"], name="uniq_summoner_champion"),
        ]
        indexes = [
            models.Index(fields=["summoner"]),
            models.Index(fields=["champion"]),
            models.Index(fields=["summoner", "champion"]),
        ]

    
