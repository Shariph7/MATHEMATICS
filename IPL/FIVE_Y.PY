import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.metrics import r2_score

df = pd.read_csv('points_table.csv')
# Fetching the records of all team of last years

Team_Performance = df.loc[df['season'] >= 2019] # Fetching the records of team performance after 2020 IPL Season
Team = Team_Performance.groupby('short_name')
net_rr = Team['nrr'].sum()
match_won = Team['matchwon'].sum()


slope, intercept, p, r, std_err = stats.linregress(net_rr, match_won)
def fun(net_rr):
    return slope * net_rr + intercept

model = list(map(fun, net_rr))
print(r)

predict = fun(net_rr)
# Create a DataFrame to store team predictions
predictions_df = pd.DataFrame({'Team': net_rr.index, 'Predicted Matches Won': predict})
predictions_df = predictions_df.sort_values(by='Predicted Matches Won', ascending=False)
# Select top 4 teams
top_4_teams = predictions_df.head(4)
print(top_4_teams)

plt.scatter(net_rr,match_won)
plt.plot(net_rr, model)
plt.show()