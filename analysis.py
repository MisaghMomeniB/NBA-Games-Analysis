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