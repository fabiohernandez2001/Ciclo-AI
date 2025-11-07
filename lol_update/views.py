import requests
from lol_navo.models import Champion, Item
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
                                hp_per_level = champion["stats"]["hpperlevel"],
                                mp = champion["stats"]["mp"],
                                mp_per_level = champion["stats"]["mpperlevel"],
                                move_speed = champion["stats"]["movespeed"],
                                armor = champion["stats"]["armor"],
                                armor_per_level = champion["stats"]["armorperlevel"],
                                spell_block = champion["stats"]["spellblock"],
                                spell_block_per_level = champion["stats"]["spellblockperlevel"],
                                attack_range = champion["stats"]["attackrange"],
                                hp_regen = champion["stats"]["hpregen"],
                                hp_regen_per_level = champion["stats"]["hpregenperlevel"],
                                crit = champion["stats"]["crit"],
                                crit_per_level = champion["stats"]["critperlevel"],
                                attack_damage = champion["stats"]["attackdamage"],
                                attack_damage_per_level = champion["stats"]["attackdamageperlevel"],
                                attack_speed = champion["stats"]["attackspeed"],
                                attack_speed_per_level = champion["stats"]["attackspeedperlevel"],
                                )
def get_items():
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version = requests.get(version_url).json()[0]
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json"
    items = requests.get(url).json()
    for key, item in items["data"].items():
        # print(key, item["name"])

        Item.objects.create(
            id = key,
            name = item["name"],
            plaintext = item["plaintext"],
            description = item["description"],
            colloq = item["colloq"],
            stacks = item["stacks"],
            depth = item["depth"],
            consumed = item["consumed"],
            consume_on_full = item["consume_on_full"],
            in_store = item["in_store"],
            hide_from_all =item["hide_from_all"],
            required_champion = item["required_champion"],
            required_ally =item["required_ally"],
            special_recipe =item["special_recipe"],
            required_buff_currency_name =item["buff_currency_name"],
            required_buff_currency_cost = item["required_buff_currency_cost"],
            base_gold = item["gold"]["base"],
            purchasable = item["gold"]["purchasable"],
            total_gold = item["gold"]["total"],
            sell_gold = item["gold"]["sell"],
            image = item["image"]["full"],
            stats = item["stats"],
            effect = item["effect"],
            builds_into = item["build_into"],
            builds_from = item["build_from"],
            tags = item["tags"],
            maps = item["maps"]
            )



# def upsert_item(item_id_str: str, raw: Dict[str, Any], version: str) -> Tuple[Item, bool]:
#     """Crea/actualiza un Item a partir del JSON crudo."""
#     try:
#         item_id = int(item_id_str)
#     except ValueError:
        # A veces hay claves no numéricas, las ignoramos
#         raise CommandError(f"Item id no numérico: {item_id_str}")

#     values = map_item_fields(raw, item_id, version)
#     obj, created = Item.objects.update_or_create(
#         id=item_id,
#         defaults=values,
#     )
#     return obj, created


