from nba_api.stats.static.teams import get_teams
import matplotlib.pyplot as plt
# import nba_api.stats.static.teams as t_imp
import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder


def one_dict(list_dict):
    keys = list_dict[0].keys()
    print(keys)
    # out_dict = {key: [] for key in keys}
    out_dict = {}
    for key in keys:
        out_dict[key] = []
    print(out_dict)  # Map<String,List<String>>
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


# print(t_imp.get_teams())
print(get_teams())
nba_teams = get_teams()
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
print(df_teams)

df_warriors_df = df_teams[df_teams['nickname'] == 'Warriors']
print(df_teams['nickname'] == 'Warriors')
print(type(df_warriors_df))
print(df_warriors_df)
warrier_id = df_warriors_df[['id']].values[0][0]
print('warrior id - ', warrier_id)

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=warrier_id)
print(gamefinder.get_json())
