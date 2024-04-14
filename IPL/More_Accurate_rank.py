import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

# Reading the CSV Files
df = pd.read_csv('table.csv')
X = df[['matchesplayed', 'matchwon']]
y = df['rank']

# Grouping columns
Team = df.groupby('short_name')
m_p = Team['matchesplayed'].sum()
m_w = Team['matchwon'].sum()

# Creating a DataFrame from net_rr and m_w
team_data = pd.DataFrame({'matchesplayed': m_p, 'matchwon': m_w})

# Resetting the index
team_data = team_data.reset_index()

regr = linear_model.LinearRegression()
regr.fit(X, y)
predictions = regr.predict(team_data[['matchesplayed', 'matchwon']])

# Clip predictions to ensure they fall within the valid range of 1 to 10
predictions = np.clip(predictions, 1, 10)
team_data['Predicted_Rank'] = predictions

# Rank the teams based on predicted ranks
team_data['Predicted_Rank'] = team_data['Predicted_Rank'].rank(method='min').astype(int)

# Introduce tie-breaking by sorting based on predicted rank and matches won
team_data = team_data.sort_values(by=['Predicted_Rank', 'matchwon'], ascending=[True, False])

# Assign unique ranks based on the sorted order
team_data['Final_Rank'] = range(1, len(team_data) + 1)

print(team_data)