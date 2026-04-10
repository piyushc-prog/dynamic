from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
    
    def process(self, text):
        sentences = []
        for line in sent_tokenize(text):  
            words = word_tokenize(line.lower())
            words = [w for w in words if w.isalpha() and w not in self.stop_words]
            if words:
                sentences.append(words)
        return sentences