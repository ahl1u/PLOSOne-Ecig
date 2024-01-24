import pandas as pd

def count_sentiments(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Count the number of positive, negative, and neutral entries
    count_positive = df['Positive'].sum()
    count_negative = df['Negative'].sum()
    count_neutral = df['Neutral'].sum()

    # Calculate the total number of entries
    total_entries = count_positive + count_negative + count_neutral

    # Calculate the proportions
    proportion_positive = count_positive / total_entries
    proportion_negative = count_negative / total_entries
    proportion_neutral = count_neutral / total_entries

    return count_positive, count_negative, count_neutral, proportion_positive, proportion_negative, proportion_neutral

if __name__ == "__main__":
    # Replace 'biweekly_sentiment_counts.csv' with the path to your CSV file
    csv_file = 'biweekly_sentiment_counts.csv'
    count_positive, count_negative, count_neutral, proportion_positive, proportion_negative, proportion_neutral = count_sentiments(csv_file)

    print(f"Number of positive entries: {count_positive}")
    print(f"Number of negative entries: {count_negative}")
    print(f"Number of neutral entries: {count_neutral}")
    print(f"Proportion of positive entries: {proportion_positive:.2f}")
    print(f"Proportion of negative entries: {proportion_negative:.2f}")
    print(f"Proportion of neutral entries: {proportion_neutral:.2f}")
