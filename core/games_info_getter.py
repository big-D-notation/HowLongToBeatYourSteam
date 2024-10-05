from howlongtobeatpy import HowLongToBeat

from .steam_api_handler import SteamApiHandler


class GamesInfoGetter:
    def get_games_info(user_id):
        api_handler = SteamApiHandler()

        game_ids = api_handler.get_games_id_list(user_id)
        game_names = api_handler.get_game_names_by_ids(game_ids)

        games_info = []

        for game_name in game_names:
            results = HowLongToBeat().search(game_name)
            if results is not None and len(results) > 0:
                result = max(results, key=lambda element: element.similarity)
                game_info = {
                    'GameName'      : result.game_name, 
                    'GameType'      : result.game_type, 
                    'MainStory'     : result.main_story, 
                    'MainExtra'     : result.main_extra, 
                    'Completionist' : result.completionist
                }

                games_info.append(game_info)

        return games_info




