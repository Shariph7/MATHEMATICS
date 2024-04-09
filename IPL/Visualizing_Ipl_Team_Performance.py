# Importing the Neccessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV Files of Points table of IPL History
df = pd.read_csv('points_table.csv')

# Dividing the Group according to the name using GroupBy aggregate functions.
df1 = df.groupby('name')
for name, rows in df1:
    print(name)
    print(rows)
df1 = df.groupby('short_name').agg({'matchesplayed' : 'sum'})
df2 = df.groupby('short_name').agg({'matchwon' : 'sum'})

# Define colors for each bar
colors = ['yellow', 'blue', 'green', 'black', 'purple', 'red', 'pink', 'cyan','skyblue','violet','red','pink','pink','orange']
plt.xlabel('Team Name')
plt.ylabel('Match PLayed!')
plt.title('IPL HISTORY')
plt.bar(df1.index,df1['matchesplayed'], color = colors)
plt.show()

# Merging
merging = pd.merge(df1,df2,on='short_name', how='outer')
print(merging)

def calculate_win_percentage(matchesplayed, matchwon):
    return (matchwon/matchesplayed) * 100

merging['Win_percentage'] = calculate_win_percentage(merging['matchesplayed'], merging['matchwon'])
print(merging)

# Visualizing the Win percentage of the IPL Team
plt.bar(merging.index,merging['Win_percentage'])
plt.show()

gp = merging.groupby('short_name')
output = merging.loc[merging['Win_percentage'] > 50]
print(output)
# BY SHARIPH THAPA