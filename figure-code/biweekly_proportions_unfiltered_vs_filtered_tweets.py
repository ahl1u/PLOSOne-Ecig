import pandas as pd

# Read data from CSV files
all_tweets_df = pd.read_csv('all_tweets.csv')
ecig_tweets_df = pd.read_csv('ecig_tweets.csv')

# Merge DataFrames on 'Biweekly Period'
merged_df = pd.merge(all_tweets_df, ecig_tweets_df, on='Biweekly Period', how='outer', suffixes=('_all', '_ecig'))

# Calculate the proportions of unfilered tweets (_all) and filtered tweets (_ecig)
merged_df['Proportion_all'] = merged_df['Count_all'] / (merged_df['Count_all'] + merged_df['Count_ecig'])
merged_df['Proportion_ecig'] = merged_df['Count_ecig'] / (merged_df['Count_all'] + merged_df['Count_ecig'])

# Save to Excel file
merged_df.to_excel('proportions_all_vs_ecig.xlsx', index=False)
