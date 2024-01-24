import json
import pandas as pd
from datetime import datetime

# Load JSON file into a list of dictionaries
with open('all_tweets.json', 'r') as file:
    tweets = [json.loads(line) for line in file]

# Create a DataFrame from the list of tweets
df = pd.DataFrame(tweets)

# Convert 'created_at' column to datetime format
df['timestamp'] = pd.to_datetime(df['created_at'], format='%a %b %d %H:%M:%S %z %Y')

# Set the 'timestamp' column as the index
df.set_index('timestamp', inplace=True)

# Group tweets biweekly and count
biweekly_tweet_count = df.resample('2W').size()

# Create a DataFrame with biweekly counts
df_counts = pd.DataFrame({'BiWeekly Period': biweekly_tweet_count.index, 'Count': biweekly_tweet_count.values})

# Save to CSV file
df_counts.to_csv('all_tweet_counts.csv', index=False)
