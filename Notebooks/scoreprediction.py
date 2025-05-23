import pandas as pd
from sportsreference.ncaab.teams import Teams
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

FIELDS_TO_DROP = ['away_points', 'home_points', 'date', 'location',
                  'losing_abbr', 'losing_name', 'winner', 'winning_abbr',
                  'winning_name', 'home_ranking', 'away_ranking']

dataset = pd.DataFrame()
print('Database Retrieving')
teams = Teams()
n = 1
for team in teams:
    dataset = pd.concat([dataset, team.schedule.dataframe_extended])
    # if n > 1:
    #     break
    n += 1
    print("Team", n, "Done")
dataset.to_csv('data-full.csv', encoding='utf-8', index=False)

# print('Database Retrieving Finished')
# X = dataset.drop(FIELDS_TO_DROP, 1).dropna().drop_duplicates()
# y = dataset[['home_points', 'away_points']].values
# X_train, X_test, y_train, y_test = train_test_split(X, y)
# parameters = {'bootstrap': False,
#               'min_samples_leaf': 3,
#               'n_estimators': 50,
#               'min_samples_split': 10,
#               'max_features': 'sqrt',
#               'max_depth': 6}
# print('Training Model')
# model = RandomForestRegressor(**parameters)
# model.fit(X_train, y_train)
# print(model.predict(X_test).astype(int), y_test)