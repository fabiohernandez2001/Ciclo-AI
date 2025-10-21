import requests
#Todas las funciones requieren de una API_Key como esta
api_key  = "RGAPI-46d300b2-0bc3-4c81-a0a7-a5ffa0ab1118"

#Función que devuelve el uuid del usuario aportando username y tag. Se puede modificar para que devuelva cualquiera de los otros campos nombrados

def get_puuid(name, tag, api_key):
    api_url  = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api_key}'
    res = requests.get(api_url)
    player_info = res.json()
    player_uuid = player_info['puuid']
    return(player_uuid)

#Ejemplo
PUUID = get_puuid("koldi", "doggy", api_key)
print( "get_uuid devuelve: "+ PUUID)

#Función que devuelve una cantidad de matchs ids personalizables a partir del count (star = 0 es el ultimo game) a partir del UUID obtenido medienta el get_puuid().
#No estoy seguro de si hay que modificar algo para que lo devuleva en formato string tal como está ahora.

def matches_ids(id, api_key, start, count):
    matchlist_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{id}/ids?type=ranked&start={start}&count={count}&api_key={api_key}"
    res = requests.get(matchlist_url).json()
    return res

#Ejemplo
Matches = matches_ids(PUUID, api_key, 0, 5)
print( "Estos son los match id de las últimas 5 partidas de koldi : " + ", ".join(Matches))

#Función que devuelve toda la información respecto a una partida a partir de un Match ID.
# Para extraer datos específicos consultar https://developer.riotgames.com/apis#match-v5/GET_getMatch

def match_info(id, api_key):
    match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{id}?api_key={api_key}"
    match_info = requests.get(match_url).json
    return match_info

#Ejemplo
Game = match_info(Matches[0], api_key)
participants = []
for player in Game["info"]["participants"]:
    participants.append(player['riotIdGameName'])
print("Estos son los nombres de usuario de cada participante de la partida: "+ ", ".join(participants))