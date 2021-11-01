class StatisticsHelper():

    def __init__(self):
        self.stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


    def generate_word_count_from_file(self, file_name):

        try:

            f = open(file_name)
            text = f.read()

            # preprocessing
            
            text = text.lower()
            text = text.replace("\n", " ")

            symbols = "!\"#$%&()*+-.,…/:;<=>?@[\]^_`{|}~\n"
            for i in symbols: 
                text = text.replace(i, " ")

            words = text.split(" ")
            words_without_stops = [word for word in words if word not in self.stopwords]
            preprocessed_words = [word for word in words_without_stops if word != ""]

            all_words_count = len(preprocessed_words)

            # word count

            wordcount = {}
            for word in preprocessed_words:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1


            sorted_x = sorted(wordcount.items(), key=lambda kv: kv[1], reverse=True)
            sorted_x_100 = sorted_x[0:100]

            words = []
            counts = []

            for item in sorted_x_100:
                words.append(item[0])
                counts.append(item[1] / all_words_count)

            print(words)
            print(counts)



            return words, counts
        
        except Exception as e:
            print(e)
            return None, None


statisticsHelper = StatisticsHelper()


