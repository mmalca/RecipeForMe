__author__ = 'mmalca'

import fasttext

def get_vector(string):
     ft = fasttext.load_model('cc.he.300.bin')
     vector = vector1 = ft.get_word_vector(string)

     return vector

