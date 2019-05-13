import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location',
                  'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
                  'winning_name']

dataset = pd.read_csv("data-full-good.csv")

X = dataset.drop(FIELDS_TO_DROP, 1)
y = dataset[['home_points', 'away_points']].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

parameters = {'bootstrap': False,
              'min_samples_leaf': 10,
              'n_estimators': 100,
              'min_samples_split': 100,
              'max_features': 'sqrt',
              'max_depth': 30}

print('Training Model')
model = RandomForestRegressor(**parameters)

model.fit(X, y)

teams = dataset['winning_abbr'].unique()
teams = np.concatenate((teams, dataset['losing_abbr'].unique()))
teams = np.unique(teams)

n = 0
teamDict = {}
for team in teams:
    teamDict[team.upper().strip()] = n
    n += 1
    
awayStats = np.zeros((n,39))

n=1
for index, game in dataset.iterrows():
    addStats = np.ndarray((39))
    addStats[0:20] = game[0:20].values
    addStats[21:36] = game[22:37].values
    addStats[37] = game['pace']
    addStats[38] = 1
    teamAbbrev = None
    if game['winner'] is 'Home':
        teamAbbrev = game['losing_abbr']
    else:
        teamAbbrev = game['winning_abbr']
    teamAbbrev = teamAbbrev.strip().upper()
    awayStats[teamDict[teamAbbrev]] += addStats
    n += 1
for team in awayStats:
    if team[-1] >= 1:
        team /= team[-1]

matchuplist = [
                ['TEXAS-TECH', 'OREGON'],
                ['KANSAS-STATE', 'KANSAS'],
            ]

for matchup in matchuplist:
    avgPace = [(awayStats[teamDict[matchup[0]]][37] + awayStats[teamDict[matchup[1]]][37])/2]

    test = pd.DataFrame([np.concatenate((awayStats[teamDict[matchup[0]]][0:37],awayStats[teamDict[matchup[1]]][0:37],avgPace)).astype(float)])
    testflip = pd.DataFrame([np.concatenate((awayStats[teamDict[matchup[1]]][0:37],awayStats[teamDict[matchup[0]]][0:37],avgPace)).astype(float)])

    y_pred = model.predict(test)
    y_predflip = model.predict(testflip)

    team1score= (y_pred[0][0] + y_predflip[0][1]) / 2
    team2score= (y_pred[0][1] + y_predflip[0][0]) / 2
        
    print(matchup[0].lower(), 'vs', matchup[1].lower(), 'Winner:', matchup[int(team1score < team2score)])