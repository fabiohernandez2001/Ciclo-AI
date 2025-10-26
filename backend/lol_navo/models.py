from django.db import models


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

    def __str__(self) -> str:
        return self.username


class Match(models.Model):
    WINNER_CHOICES = (
        (100, "Blue"),
        (200, "Red"),
    )

    duration = models.DurationField()
    winner_team = models.PositiveSmallIntegerField(choices=WINNER_CHOICES)
    time_lane = models.CharField(max_length=100)
    gold_diff = models.PositiveBigIntegerField()
    summoners = models.ManyToManyField(
        Summoner,
        through="MatchSummoners",
        through_fields=("match", "summoner"),
        related_name="matches",
    )

    def __str__(self) -> str:
        return f"Match {self.pk}"


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
        through="ChampionStat",
        through_fields=("champion", "summoner"),
        related_name="champions",
    )

    def __str__(self) -> str:
        return self.champion_name


class Rune(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    rune_name = models.CharField(max_length=20)
    rune_value = models.PositiveSmallIntegerField()
    rune_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.rune_name


class Item(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    item_name = models.CharField(max_length=20)
    item_value = models.PositiveSmallIntegerField()
    item_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.item_name


class MatchSummoners(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="participants",
    )
    summoner = models.ForeignKey(
        Summoner,
        on_delete=models.CASCADE,
        related_name="participations",
    )
    champion = models.ForeignKey(
        Champion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="match_entries",
    )
    skill_order = models.CharField(max_length=255, blank=True, default="")
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
            models.UniqueConstraint(
                fields=("match", "summoner"),
                name="uniq_match_summoner",
            ),
        ]
        indexes = [
            models.Index(
                fields=("match",),
                name="lol_navo_ma_match_i_a43a6d_idx",
            ),
            models.Index(
                fields=("summoner",),
                name="lol_navo_ma_summone_608e1a_idx",
            ),
            models.Index(
                fields=("match", "summoner"),
                name="lol_navo_ma_match_i_e32db8_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.match_id} | {self.summoner_id}"


class ChampionStat(models.Model):
    summoner = models.ForeignKey(
        Summoner,
        on_delete=models.CASCADE,
        related_name="champion_stats",
    )
    champion = models.ForeignKey(
        Champion,
        on_delete=models.CASCADE,
        related_name="summoner_stats",
    )
    champion_point = models.PositiveBigIntegerField(default=0)
    champion_winrate = models.FloatField(default=0.0)
    champion_kda = models.FloatField(default=0.0)
    champion_games = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("summoner", "champion"),
                name="uniq_summoner_champion",
            ),
        ]
        indexes = [
            models.Index(
                fields=("summoner",),
                name="lol_navo_ch_summone_7dee11_idx",
            ),
            models.Index(
                fields=("champion",),
                name="lol_navo_ch_champio_e7a704_idx",
            ),
            models.Index(
                fields=("summoner", "champion"),
                name="lol_navo_ch_summone_3c06f4_idx",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.summoner_id} | {self.champion_id}"
