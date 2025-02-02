import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

df['Date'] = pd.datetime(df['Date'])
df['Home Win'] = df['Winner'] == df['Home Team']