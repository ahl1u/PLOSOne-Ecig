import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# Read the data
df = pd.read_csv('sentiment_classification_result.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Re-assign labels in 'vape_user'
df['vape_user'] = df['vape_user'].map({'y': 'User', 'n': 'Non-user'})

# Set the timestamp as the index
df.set_index('timestamp', inplace=True)

# Group by two weeks and 'vape_user', then count unique user_ids
df_grouped = df.groupby([pd.Grouper(freq='2W'), 'vape_user'])['user_id'].nunique().unstack(fill_value=0)

# Reorder columns
df_grouped = df_grouped[['User', 'Non-user']]

# Convert to proportions
df_grouped = df_grouped.div(df_grouped.sum(axis=1), axis=0)

# Create a separate index for the CSV, showing labels only at the start of each month
csv_index = df_grouped.index.to_series().apply(lambda x: x.strftime('%m/%d/%Y') if x.is_month_start else '')

# Plot
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(df_grouped.index, df_grouped['User'], color="blue", label='User')
ax.plot(df_grouped.index, df_grouped['Non-user'], color="red", label='Non-user')

# Format x-axis labels
date_form = DateFormatter("%m/%d/%Y")
ax.xaxis.set_major_formatter(date_form)

# Set major tick at every month
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Additional Plotting settings
plt.xlabel('Month')
plt.ylabel('Proportion of Unique Users')
plt.legend()
plt.grid()
plt.gcf().autofmt_xdate()  # Rotation
plt.show()

# Remove the time and timezone info from the index
df_grouped.index = df_grouped.index.tz_localize(None).strftime('%m/%d/%Y')

# Create a new index for CSV where only the start of each month is labeled
csv_index = [label if pd.Timestamp(label).is_month_start else '' for label in df_grouped.index]

# Save the DataFrame using the customized index
df_grouped.index = csv_index
df_grouped.to_csv('output_for_excel.csv', index_label='timestamp')

