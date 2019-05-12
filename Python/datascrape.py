import pandas as pd
from sportsreference.ncaab.teams import Teams

dataset = pd.DataFrame()
teams = Teams()
print("Total Teams:",len(teams))
totalTeams = len(teams)
n = 0
for team in teams:
    dataset = pd.concat([dataset, team.schedule.dataframe_extended])
    n += 1
    print(n, "of", totalTeams, "Done")
dataset.to_csv('data-full.csv', encoding='utf-8', index=False)