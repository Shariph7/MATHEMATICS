import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV Files of Points table of IPL History
df = pd.read_csv('points_table.csv')

# Grouping the data by team short name
df1 = df.groupby('short_name').agg({'matchesplayed': 'sum'})
df2 = df.groupby('short_name').agg({'matchwon': 'sum'})

# Merging the data
merging = pd.merge(df1, df2, on='short_name', how='outer')

# Define a function to calculate win percentage
def calculate_win_percentage(matches_played, matches_won):
    return (matches_won / matches_played) * 100

# Applying the function to calculate win percentage
merging['win_percentage'] = calculate_win_percentage(merging['matchesplayed'], merging['matchwon'])

# Visualizing the Win percentage of the IPL Team
plt.bar(merging.index, merging['win_percentage'], color='orange')
plt.xlabel('Team Name')
plt.ylabel('Win Percentage')
plt.title('IPL Teams Win Percentage')
plt.xticks(rotation=45)
plt.show()