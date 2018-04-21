import gensim
from gensim.models import KeyedVectors
import numpy as np

from utils.utils import split_reviews

word_vectors = KeyedVectors.load_word2vec_format('../dataset/GoogleNews-vectors-negative300.bin', binary=True)
# if you vector file is in binary format, change to binary=True

x = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])

x = word_vectors.get_vector('does')

y = x + x

t = str_to_list("abds asd")

x = [1,2]
y = x[:-3:-1]

import string
from nltk import word_tokenize

def str_to_list(line=''):
    identify = string.maketrans('', '')
    delEStr = string.punctuation +'0123456789'
    cleanLine =line.translate(identify,delEStr)
    result=word_tokenize(cleanLine)
    return result

X = range(10)

y = split_reviews(X)
print(y)