import pandas as pd

# Load your data from a CSV file
df = pd.read_csv('1positive_sentiment.csv')

# Remove newline characters within each tweet
df['text'] = df['text'].str.replace('\n', ' ')

# Keep only 'text' column
df = df[['text']]

# Save the reduced DataFrame to a new CSV file
df.to_csv('reduced_tweets_positive.csv', index=False)
