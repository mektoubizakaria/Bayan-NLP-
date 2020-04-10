import pickle
import warnings

def predict(article):
    texts=[article]
    print("load the model... ",end='', flush=True)
    with open('F:/cours/Master/S3/web_text_mining/text_class/ai-text-classification/models/models/pickle_model_arabic.pkl', 'rb') as file:
        pickle_model = pickle.load(file)
    print("ok")

    print("text verctorizing... ",end='', flush=True)
    with open('F:/cours/Master/S3/web_text_mining/text_class/ai-text-classification/models/vectorizer/pickle_tfidf_arabic.pkl', 'rb') as file2:
        pickle_tfidf = pickle.load(file2)
    warnings.filterwarnings("ignore")
    text_features = pickle_tfidf.transform(texts)
    print("ok ")

    print("text classification... ",end='', flush=True)
    id_to_category= {0:'sport',1:'politique',2:'economie',3:'art-et-culture	'}
    predictions = pickle_model.predict(text_features)
    print("ok")
    for text, predicted in zip(texts, predictions):
        return id_to_category[predicted]