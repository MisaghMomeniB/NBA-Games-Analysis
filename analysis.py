# Import necessary libraries for data manipulation, visualization, and analysis
import pandas as pd  # For data handling and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For advanced and aesthetically pleasing visualizations

# Load the data into a Pandas DataFrame
df = pd.read_csv('data.csv')  # Convert the string data into a DataFrame

# Convert the 'Date' column to datetime format for easier date-based analysis
df['Date'] = pd.to_datetime(df['Date'])

# Add a new column 'Home Win' to indicate whether the home team won the game
df['Home Win'] = df['Winner'] == df['Home Team']

# Display basic statistics for numerical columns in the dataset
print("Basic Statistics:")
print(df.describe())  # Provides summary statistics like mean, std, min, max, etc.

# Calculate the number of wins for each team (both home and away games)
wins_by_team = pd.concat([df['Home Team'][df['Home Win']], df['Away Team'][~df['Home Win']]]).value_counts()
print("\nNumber of Wins for Each Team:")  # Print the win counts for each team
print(wins_by_team)

# Calculate the average scores for home and away teams
home_scores_avg = df['Home Score'].mean()  # Average score when playing at home
away_scores_avg = df['Away Score'].mean()  # Average score when playing away
print(f"\nAverage Home Scores: {home_scores_avg:.2f}")  # Print the average home score
print(f"Average Away Scores: {away_scores_avg:.2f}")  # Print the average away score

# Visualize the number of wins for each team using a bar chart
plt.figure(figsize=(12, 6))  # Set the figure size for better readability
sns.barplot(x=wins_by_team.index, y=wins_by_team.values, palette="viridis")  # Create a bar plot
plt.title("Number of Wins for Each Team")  # Add a title to the chart
plt.xlabel("Team Name")  # Label for the x-axis
plt.ylabel("Number of Wins")  # Label for the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()  # Display the chart

# Visualize the comparison of average home and away scores using a bar chart
scores = pd.DataFrame({
    'Type': ['Home', 'Away'],  # Define categories for the chart
    'Average Score': [home_scores_avg, away_scores_avg]  # Provide average scores
})
sns.barplot(x='Type', y='Average Score', data=scores, palette="coolwarm")  # Create the bar plot
plt.title("Comparison of Average Home and Away Scores")  # Add a title to the chart
plt.ylabel("Average Score")  # Label for the y-axis
plt.show()  # Display the chart