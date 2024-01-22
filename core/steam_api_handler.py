import requests

from config import API_KEY


class SteamApiHandler:
    def __init__(self):
        self.api_key = API_KEY

    def get_games_id_list(self, user_id):
        endpoint  = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={user_id}&format=json'

        response = requests.get(endpoint)

        if response.status_code == 200:
            games_id = [
                game['appid'] 
                for game in response.json()['response']['games']
            ]

            return games_id
            
        else:
            print(f'Error: {response.status_code}')
            print(response.text)

    def get_game_names_by_ids(self, ids):
        names = []

        endpoint = f'http://api.steampowered.com/ISteamApps/GetAppList/v2/'

        response = requests.get(endpoint)

        if response.status_code == 200:
            app_list = response.json().get('applist', {}).get('apps', [])
            app_id_to_name = {app['appid']: app['name'] for app in app_list}

            for app_id in ids:
                app_name = app_id_to_name.get(app_id, 'Unknown Game')
                names.append(app_name)

        else:
            print(f"Error: {response.status_code}")
            print(response.text)

        return names

