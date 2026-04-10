from data.fetcher import DataFetcher
from preprocessing.cleaner import TextCleaner
from model.word2vec import Word2VecModel
from utils.helper import chose_model
from textblob import TextBlob
from spellchecker import SpellChecker
import config

spell = SpellChecker()
def correct_spelling(word):
    return spell.correction(word)
trainer = None
def train_model():
    global trainer


    url = input("Enter URL: ")

    fetcher = DataFetcher()
    raw_text = fetcher.fetch_from_url(url)


    cleaner = TextCleaner()
    sentences = cleaner.process(raw_text)

    if not sentences:
        print("No data found")
        exit()


    sg = chose_model()


    trainer = Word2VecModel(
        vector_size=config.VECTOR_SIZE,
        window=config.WINDOW,
        min_count=config.MIN_COUNT,
        sg=sg
    )

    trainer.train(sentences, config.EPOCHS)

    save = input("Do you want to save this model: y/n")
    if save == 'y':
        path = input("please enter the file name")
        trainer.save_model(path)
        print("model saved successfully")
def label_model():
    global trainer
    path = input("enter the file name")
    trainer = Word2VecModel(
        vector_size= config.VECTOR_SIZE,
        window=config.WINDOW,
        min_count=config.MIN_COUNT,
        
        
    )
    try:
        trainer.load_model(path)
        print('successfully load the model')
    except:
        print('error loading model')
def query_model():
    global trainer

    if trainer is None or not trainer.is_trained:
        print("no model loaded")
        return
    while True:
        word = input("\n enter word (or back)").lower()
        word  = str(TextBlob(word).correct())
        
        words = correct_spelling(word)
        if words == 'back':
            break

        result = trainer.get_similar_words(word)
        if result == 'word not found':
            print(result)
        else:
            for similar_word, score in result:
                print(f"{similar_word} -> {score:.3f}") 

def main():
    while True:
        print('\---MENU---/')
        print('press 1 to train the model')
        print('press 2 label model')
        print('press 3 querry model ')
        print('press 4 to exit')

        choice = int(input('please enter your chooice'))
        if choice == 1:
            train_model()
        elif choice ==2:
            label_model()
        
        elif choice == 3:
            query_model()
        elif choice ==4:
            print("exiting")
            break
        else:
            print('Invalid chooice')


if __name__ == "__main__":
    main()






