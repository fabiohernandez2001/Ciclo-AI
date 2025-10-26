from django.contrib import admin

from .models import Summoner, Match, MatchSummoners, Champion, ChampionStat, Item, Rune

admin.site.register(Summoner)
admin.site.register(Match)
admin.site.register(MatchSummoners)
admin.site.register(Champion)
admin.site.register(ChampionStat)
admin.site.register(Item)
admin.site.register(Rune)
