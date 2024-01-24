import ujson
import nltk
from nltk.tokenize import word_tokenize

class ecigFiltering:

    keywords = ["e-cig", "e-cigs", "ecig", "ecigs", "electroniccigarette", "vape", "vapers", "vaping", "vapes", "e-liquid", "ejuice", "eliquid", "e-juice", "vapercon", "vapeon", "vapefam", "vapenation", "juul"]

    def main(self):
        self.filter_ecig()

    def contains(self, line):  #detect whether those ecig-related keywords are in the Twitter content
        if "delete" in line:  # Exclude deletions
            return False

        string = line.get("text", "")  # Use the tweet text
        if string.lower().startswith("rt @"):  # Exclude retweets
            return False

        string = string.lower()   # Make the tweets in lower case
        string = word_tokenize(string)   # Tokenize the tweets by space

        return any(s in string for s in self.keywords)

    def filter_ecig(self):
        with open("filtered_ecig.json", 'w') as output: #output filename
            with open("Jun27.json", 'rb') as src: #input filename
                for line in src:
                    parsedJsonRecord = ujson.decode(line)
                    if self.contains(parsedJsonRecord):
                        filteredJsonRecord = {field: parsedJsonRecord[field] for field in ['created_at', 'id', 'id_str', 'text', 'truncated', 'user'] if field in parsedJsonRecord}
                        if parsedJsonRecord.get("truncated", True):
                            filteredJsonRecord["full_text"] = parsedJsonRecord.get("extended_tweet", {}).get("full_text", None)
                        else:
                            filteredJsonRecord["full_text"] = 'null'
                        output.write(ujson.dumps(filteredJsonRecord) + '\n')

        output.close()
        src.close()


if __name__ == '__main__':
    ecigFiltering().main()
