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

    def __str__(self) -> str:
        return self.username


class Match(models.Model):
    WINNER_CHOICES = (
        (100, "Blue"),
        (200, "Red"),
    )
    id = models.CharField(primary_key=True, max_length=32)
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
    name = models.CharField(max_length=16, default = "")
    title = models.CharField(max_length=20, default = "")
    description = models.CharField(max_length=2550, default = "")
    attack = models.PositiveSmallIntegerField(default=0)
    defense = models.PositiveSmallIntegerField(default=0)
    magic = models.PositiveSmallIntegerField(default=0)
    difficulty = models.PositiveSmallIntegerField(default=0)
    tags = models.JSONField(default= {'tags': []})
    partype = models.CharField(default = "")
    hp = models.FloatField(default=0)
    hpperlevel = models.FloatField(default=0)
    mp = models.FloatField(default=0)
    mpperlevel = models.FloatField(default=0)
    movespeed = models.FloatField(default=0)
    armor = models.FloatField(default=0)
    armorperlevel = models.FloatField(default=0)
    spellblock = models.FloatField(default=0)
    spellblockperlevel = models.FloatField(default=0)
    attackrange = models.PositiveSmallIntegerField(default=0)
    hpregen = models.FloatField(default=0)
    hpregenperlevel = models.FloatField(default=0)
    mpregen = models.FloatField(default=0)
    mpregenperlevel = models.FloatField(default=0)
    crit = models.FloatField(default=0)
    critperlevel = models.FloatField(default=0)
    attackdamage = models.FloatField(default=0)
    attackdamageperlevel = models.FloatField(default=0)
    attackspeedperlevel = models.FloatField(default=0)
    attackspeed = models.FloatField(default=0)
    wins = models.FloatField(default=0)
    bans = models.FloatField(default=0)
    picks = models.FloatField(default=0)
    icon = models.URLField(default="")
    summoners = models.ManyToManyField(
        Summoner,
        through="ChampionStat",
        through_fields=("champion", "summoner"),
        related_name="champions",
    )
    def __str__(self) -> str:
        return self.name



class Rune(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    rune_name = models.CharField(max_length=20)
    rune_value = models.PositiveSmallIntegerField()
    rune_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.rune_name


class Item(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=20, default = "")
    description = models.CharField(max_length=200, default="")
    plaintext = models.CharField(max_length=255, blank=True, default="")
    value = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True, default="")  # HTML de Riot
    colloq = models.CharField(max_length=255, blank=True)  # términos de búsqueda
    # Propiedades varias del ítem
    stacks = models.PositiveIntegerField(null=True, blank=True)
    depth = models.PositiveIntegerField(null=True, blank=True)
    consumed = models.BooleanField(default=False)
    consume_on_full = models.BooleanField(default=False)
    in_store = models.BooleanField(default=True)
    hide_from_all = models.BooleanField(default=False)
    # Requisitos especiales
    required_champion = models.CharField(max_length=32, blank=True)
    required_ally = models.CharField(max_length=32, blank=True)
    special_recipe = models.PositiveIntegerField(null=True, blank=True)
    required_buff_currency_name = models.CharField(max_length=64, blank=True)
    required_buff_currency_cost = models.PositiveIntegerField(null=True, blank=True)
    # gold: { "base": int, "purchasable": bool, "total": int, "sell": int }
    base_gold = models.IntegerField(default = 0)
    purchasable = models.BooleanField(default = False)
    total_gold = models.IntegerField(default = 0)
    sell_gold = models.IntegerField(default = 0)
    # image: { "full": str, "sprite": str, "group": str, "x": int, "y": int, "w": int, "h": int }
    image = models.URLField(default = "")
        # stats: diccionario de stats (p.ej. AbilityHaste, MagicResist, etc.)
    stats = models.JSONField(default=dict, blank=True)
    # effect: efectos/variables usadas en la description (p.ej. "Effect1Amount": "15")
    effect = models.JSONField(default=dict, blank=True)
    # Listas y banderas por mapa / tags
    # into / from: listas de IDs de ítems (construcciones)
    builds_into = ArrayField(models.PositiveIntegerField(), default=list, blank=True)  # "into"
    builds_from = ArrayField(models.PositiveIntegerField(), default=list, blank=True)  # "from"
    # tags: lista de etiquetas (Armor, AttackSpeed, Mana, etc.)
    tags = ArrayField(models.CharField(max_length=32), default=list, blank=True)
    # maps: {"11": true/false, "12": true/false, ...}
    maps = models.JSONField(default=dict, blank=True)
    # Metadatos opcionales




    def __str__(self) -> str:
        return self.item_name


class MatchSummoners(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="match_entries",
    )
    summoner = models.ForeignKey(
        Summoner,
        on_delete=models.CASCADE,
        related_name="participants",
    )
    champion = models.ForeignKey(
        Champion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="champion",
    )
    item0 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item0",
    )
    item1 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item1",
    )
    item2 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item2",
    )
    item3 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item3",
    )
    item4 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item4",
    )
    item5 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item5",
    )
    item6 = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="item6",
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
        related_name="stats",
    )
    champion = models.ForeignKey(
        Champion,
        on_delete=models.CASCADE,
        related_name="summoner_stats",
    )
    point = models.PositiveBigIntegerField(default=0)
    winrate = models.FloatField(default=0.0)
    kda = models.FloatField(default=0.0)
    games = models.PositiveIntegerField(default=0)

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
        return f"{self.summoner_id} | {self.id}"
