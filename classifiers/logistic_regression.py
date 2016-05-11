import math
import matplotlib.pyplot as plt

#Regex for parsing bounded words
vectorizer = token_pattern(token_pattern=r'\b\w+\b')

word_count = {}
n = 0
correct = 0

#TODO implement gradient descent for picking most likely coefficients

#Remove punctuation so words with puncuation are treated the same e.g. Dog! Dog.
def remove_puncuation(text):
    import string
    return text.translate(None, string.punctuation)
    

def predict(score):
    return 1 if score > 0 else 0

def score(xi):
    return xi['good'] + 1.5 * xi['great'] + -1 * ['bad'] + -1.5 * xi['awful'] # :x

def probability(score):
    return 1 / 1 + math.exp(-score)
    
def accuracy():
    return correct / n