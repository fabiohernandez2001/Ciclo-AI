import requests
from lol_navo.models import Champion
def test():
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version = requests.get(version_url).json()
    version = version[0]

    champion_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/es_ES/champion.json"
    champions = requests.get(champion_url).json()
    for champion in champions["data"].values():
        Champion.objects.create (id = champion["key"],
                                icon = f"https://ddragon.leagueoflegends.com/cdn/15.21.1/img/champion/{champion["image"]["full"]}.png",
                                champion_name = f"{champion["name"]}",
                                champion_role = "none",
                                champion_description = f"{champion["blurb"]}")
