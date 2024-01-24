import pandas as pd

# Read data from a CSV file
df = pd.read_csv('sentiment_classification_result_roBERTa.csv')

# Count the number of 'y' and 'n' in the 'vape_user' column
counts = df['vape_user'].value_counts()

print('Number of vape users (y):', counts['y'])
print('Number of non-vape users (n):', counts['n'])


# Count the number of 'y' and 'n' in the 'vape_user' column
counts = df['sentiment_score'].value_counts()

print('Number of positive:', counts[1])
print('Number of negative:', counts[-1])
print('Number of neutral:', counts[0])
