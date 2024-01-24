import pandas as pd

# Read data from a CSV file
df = pd.read_csv('sentiment_classification_result_roBERTa.csv')

# Create two separate dataframes based on 'vape_user' column
df_y = df[df['vape_user'] == 'y']
df_n = df[df['vape_user'] == 'n']

# Save these dataframes into two separate CSV files
df_y.to_csv('sentiment_classification_result_roBERTa_vape_users.csv', index=False)
df_n.to_csv('sentiment_classification_result_roBERTa_non_vape_users.csv', index=False)