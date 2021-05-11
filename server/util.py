import json
import pickle
import numpy as np

__teams = None
__data_columns = None
__model = None
__venue_columns = None

def get_estimated_score(venue,innings,ball,batting_team,bowling_team):
    x = np.zeros(33)
    x[1] = innings
    x[2] = ball
    try:
        loc_venue = __venue_columns.index(venue.lower())
        loc_index_batting = __data_columns.index(batting_team.lower())
        loc_index_bowling =__data_columns.index(bowling_team.lower())
    except:
        loc_venue = -1
        loc_index_batting = -1
        loc_index_bowling = -1
    if loc_index_batting >=0:
        x[loc_index_batting] = 1
    if loc_index_bowling >= 0:
        x[loc_index_bowling] = 1
    if loc_venue >=0:
        x[0] = float(loc_venue)

    return __model.predict([x])[0]
def get_columns():
    return(list(__data_columns[3:]))
def get_venues():
    return(list(__venue_columns))
def load_saved_artifacts():
    print("Loading....")
    global __data_columns
    global __teams
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __teams = __data_columns[3:]
    global __model
    global __venue_columns
    with open("./artifacts/encoded_venue.json",'r') as f:
        __venue_columns = json.load(f)['encoded_venues']
    with open("./artifacts/ipl_matches_prediction.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading is done")
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_columns())
    print(get_estimated_score('Sharjah Cricket Stadium',1.0,1.3,'batting_team_Delhi Daredevils','bowling_team_Royal Challengers Bangalore'))