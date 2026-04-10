from gensim.models import Word2Vec

class Word2VecModel:
    def __init__(self, vector_size, window, min_count, sg):
        self.model = Word2Vec(
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            sg=sg
        )
        self.is_trained = False
    
    def train(self, sentences, epochs):
        if not sentences:
            raise ValueError("No sentences provided for training")
        self.model.build_vocab(sentences)
        self.model.train(
            sentences,
            total_examples=len(sentences),
            epochs=epochs
        )
        self.is_trained = True
        print("Vocabulary size:", len(self.model.wv))
    
    def get_similar_words(self, word):
        if not self.is_trained:
            return "Model not trained yet"
        
        word = word.lower()
        
        if word in self.model.wv:
            return self.model.wv.most_similar(word)
        
        return "word not found"
    
    def save_model(self, path="model.model"):
        self.model.save(path)
    
    def load_model(self, path="model.model"):
        self.model = Word2Vec.load(path)
        self.is_trained = True