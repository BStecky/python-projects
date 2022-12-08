from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_games():
    scoreboard = get_links()['leagueSchedule']
    games = get(BASE_URL +  scoreboard).json()['league']['standard']
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        start_data = game['startTimeUTC']
    #     # clock = game['clock']
    #     # period = game['period']

        print("------------------------------------------")
    #     # print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team} - {away_team}")
        print(f"Start time: {start_data}")
    #     print(f"{clock} - {period['current']}")

get_games()





