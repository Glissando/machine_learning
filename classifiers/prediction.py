#import sframe
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

#Regex for parsing bounded words
vectorizer = token_pattern(token_pattern=r'\b\w+\b')

word_count = {}

train_matrix = vectorizer.fit_transform(train_data['review_clean'])

test_matrix = vectorizer.transform(test_data['review_clean'])

#Remove punctuation so words with puncuation are treated the same e.g. Dog! Dog.
def remove_puncuation(text):
    import string
    return text.translate(None, string.punctuation)
    
def train():
    logit = LogisticRegression()
    logit.fit(train_matrix)