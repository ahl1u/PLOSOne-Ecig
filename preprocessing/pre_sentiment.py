import ujson
import csv
from glob import glob

# Define a list to store the data
data = []

# Loop over all JSON files
for filename in glob('filtered_ecig_promo_flavor.json'):
    with open(filename, 'r') as input_file:
        print(filename)

        # Loop over each line in the file
        for line in input_file:
            try: 
                # Decode the line as JSON
                line = ujson.decode(line)
                # Extract the relevant fields
                user_id = line['user']['id_str'] # Get the 'id_str' from the 'user' dictionary.
                date = line['created_at'] # Get the 'created_at' field directly.
                tweet = line['text'] if line['full_text'] == "null" else line['full_text'] # Get the 'text' or 'full_text' field directly.
                # Add the data to the list
                data.append([user_id, date, tweet])
            except Exception as e:
                # If anything goes wrong, print an error message and skip this line
                print(f"Failed to process line due to {str(e)}")
                continue

# Write the data to a CSV file
with open('pre_sentiment.csv', 'w', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['user_id', 'date', 'tweet'])
    for entry in data:
        writer.writerow(entry)
