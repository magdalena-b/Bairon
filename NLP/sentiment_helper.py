from nltk.tokenize import sent_tokenize
import text2emotion
import itertools
class SentimentHelper():
    def __init__(self) -> None:
        pass
    
    def mean_average(json_a, json_b, count):
        try:
            for key_1, key_2 in zip(json_a, json_b):
                json_a[key_1] = (json_a[key_1] * count + json_b[key_2]) / (count + 1)
                json_a[key_1] = round(json_a[key_1], 6)
            return json_a
        except Exception as e:
            print(e)
            return None

    def generate_avg_sa(self, file_name):
        try:
            f = open(file_name)
            text = f.read()
            table = text.split("\n\n")
            sentiment_table = {}
            poem_counter = 0
            for poem in table:
                if(poem_counter == 0):
                    sentiment_table = text2emotion.get_emotion(poem)
                else:
                    sentiment_table = SentimentHelper.mean_average(sentiment_table, text2emotion.get_emotion(poem), poem_counter)
                poem_counter += 1
            return sentiment_table
        except Exception as e:
            print(e)
            return None

sentimentHelper = SentimentHelper()