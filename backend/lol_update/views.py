from django.shortcuts import render
import requests
from lol_navo.models import Champion
# Create your views here.
def get_champions():
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version = requests.get(version_url).json()
    version = version[0]
    champion_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/es_ES/champion.json"
    champions = requests.get(champion_url).json()
    for champion in champions["data"].values():
        Champion.objects.create (id = champion["key"],
                                icon = f"https://ddragon.leagueoflegends.com/cdn/15.21.1/img/champion/{champion["image"]["full"]}",
                                name = f"{champion["name"]}",
                                tags = champion["tags"],
                                title = champion["title"],
                                description = f"{champion["blurb"]}",
                                attack = champion["info"]["attack"],
                                defense = champion["info"]["defense"],
                                magic = champion["info"]["magic"],
                                difficulty = champion["info"]["difficulty"],
                                partype = champion["partype"],
                                hp = champion["stats"]["hp"],
                                hpperlevel = champion["stats"]["hpperlevel"],
                                mp = champion["stats"]["mp"],
                                mpperlevel = champion["stats"]["mpperlevel"],
                                movespeed = champion["stats"]["movespeed"],
                                armor = champion["stats"]["armor"],
                                armorperlevel = champion["stats"]["armorperlevel"],
                                spellblock = champion["stats"]["spellblock"],
                                spellblockperlevel = champion["stats"]["spellblockperlevel"],
                                attackrange = champion["stats"]["attackrange"],
                                hpregen = champion["stats"]["hpregen"],
                                hpregenperlevel = champion["stats"]["hpregenperlevel"],
                                crit = champion["stats"]["crit"],
                                critperlevel = champion["stats"]["critperlevel"],
                                attackdamage = champion["stats"]["attackdamage"],
                                attackdamageperlevel = champion["stats"]["attackdamageperlevel"],
                                attackspeed = champion["stats"]["attackspeed"],
                                attackspeedperlevel = champion["stats"]["attackspeedperlevel"],
                                )