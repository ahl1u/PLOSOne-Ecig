import ujson
import pandas as pd



class FlavorFiltering:

    keyword_file = "Key-words.xlsx" #favor list excel file
    keywords = []


    def extract_keywords(self):
        input_keyword_file = pd.read_excel(self.keyword_file, engine='openpyxl') #read excel file
        self.keywords = [x for x in input_keyword_file.iloc[:, 1].tolist() if isinstance(x,str)] #take flavor names as keywords, which is the column with index 1
        self.neg_keywords = [x for x in input_keyword_file.iloc[:, 2].tolist() if isinstance(x, str)]#flavor names as neg keywords, column w/ index 2

    def main(self):
        self.extract_keywords() 
        print(self.keywords)
        print(self.neg_keywords)
        self.filter_flavor()

    def contains(self, line):
        if line.get("truncated", False):
            string = line.get("extended_tweet", {}).get("full_text", "").lower()
        else:
            string = line.get("text", "").lower()

        if string.startswith("rt @"):  # Exclude retweets
            return False

        # Check for negative phrases in the text
        for l in self.neg_keywords:
            if l.lower() in string:
                return False

        # Check for positive phrases in the text, only if no negative phrase was found
        for s in self.keywords:
            if s.lower() in string.split(' '):  # Check for whole word match
                return True

        return False


    def filter_flavor(self):
        with open("filtered_ecig_promo_flavor.json", 'w') as output, open("filtered_ecig_promo.json", 'rb') as src:
            for line in src:
                parsedJsonRecord = ujson.decode(line)
                if self.contains(parsedJsonRecord):
                    output.write(ujson.dumps(parsedJsonRecord) + '\n')

        output.close()
        src.close()


if __name__ == '__main__':
    flt = FlavorFiltering()
    flt.main()