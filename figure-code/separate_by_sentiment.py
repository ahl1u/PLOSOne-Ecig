import pandas as pd

# Load your data from a CSV file
df = pd.read_csv('sentiment_classification_result_roBERTa.csv')

# Ensure that sentiment_score is of integer type
df['sentiment_score'] = df['sentiment_score'].astype(int)

# Now, save three separate CSV files for -1, 0, 1 sentiment
df[df['sentiment_score'] == -1].to_csv('1negative_sentiment.csv', index=False)
df[df['sentiment_score'] == 0].to_csv('1neutral_sentiment.csv', index=False)
df[df['sentiment_score'] == 1].to_csv('1positive_sentiment.csv', index=False)