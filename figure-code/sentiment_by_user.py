import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the file
df = pd.read_csv('sentiment_classification_result_roBERTa.csv')

# Map 'vape_user' to 'vapers' and 'non-vapers'
df['vape_user'] = df['vape_user'].map({'y': 'vapers', 'n': 'non-vapers'})

# Map 'sentiment_score' to 'Negative', 'Neutral', 'Positive'
df['sentiment_score'] = df['sentiment_score'].map({-1: 'Negative', 0: 'Neutral', 1: 'Positive'})

# Group by 'vape_user' and 'sentiment_score' and count the number of posts
grouped_df = df.groupby(['vape_user', 'sentiment_score']).size().unstack(fill_value=0)

# Normalize to proportions
grouped_df = grouped_df.div(grouped_df.sum(axis=1), axis=0)

# Plotting
ax = grouped_df.plot(kind='bar', stacked=False, figsize=(10,6), color=["red", "green", "blue"])
plt.xlabel('User Category')
plt.ylabel('Proportion')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability

# Get legend and modify legend labels
legend = ax.get_legend()
legend.set_title('Sentiment Category')
labels = ['Negative', 'Neutral', 'Positive']
for text, label in zip(legend.get_texts(), labels):
    text.set_text(label)

# Increase y limit
plt.ylim(0, 0.9)

# Print the values in a format you can directly copy-paste into Excel
print("User Category, Sentiment Category, Proportion")
for i, row in grouped_df.iterrows():
    for j, value in row.iteritems():
        print(f"{i}, {j}, {value}")


plt.show()

