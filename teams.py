import requests
import json

#Calling API
response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
print("Status Code: ", response.status_code)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

data = response.json()["teams"]

def getBestHomeTeam():
    pass

def getBestAwayTeam(): 
    pass

def getOffensiveHomeTeam():
    best_offensive_team = []
    for element in data:
        best_offensive_team.append([element["id"], element["strength_attack_home"]])
    offensive_score = float("-inf")
    best_team = None
    for team in best_offensive_team:
        if team[1] > offensive_score:
            offensive_score = team[1]
            best_team = team[0]
    for o in data:
        if o["id"] == best_team:
            print("Best offensive team \n", o["name"])
            return o
    return None


def getDefensiveHomeTeam():
    pass

def getOffensiveAwayTeam():
    pass

def getDefensiveAwayTeam():
    pass