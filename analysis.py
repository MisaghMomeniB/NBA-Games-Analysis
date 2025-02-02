import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

df['Date'] = pd.datetime(df['Date'])
df['Home Win'] = df['Winner'] == df['Home Team']

print("All : ")
print(df.describe())

# Number of wins for each team
wins_by_team = pd.concat([df['Home Team'][df['Home Win']], df['Away Team'][~df['Home Win']]]).value_counts()
print("\nNumber of wins for each team:")
print(wins_by_team)

# Average scores for home and away teams
home_scores_avg = df['Home Score'].mean()
away_scores_avg = df['Away Score'].mean()
print(f"\nAverage home scores: {home_scores_avg:.2f}")
print(f"Average away scores: {away_scores_avg:.2f}")

# 4. Data visualization
plt.figure(figsize=(12, 6))

# Bar chart showing the number of wins for each team
sns.barplot(x=wins_by_team.index, y=wins_by_team.values, palette="viridis")
plt.title("Number of Wins for Each Team")
plt.xlabel("Team Name")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()