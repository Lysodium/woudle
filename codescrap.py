import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

vowels = {'a','e','i','o','u'}
freq = {'s':0.3, 'o':0.04, 'f':0.01, 'a':0.2, 't':0.14, 'e':0.25}
order = {('s',1):0.51, ('s',2):0.41,('s',3):0.31,  ('s',4):0.21, ('s',5):0.11, 
        ('o',1):0.52, ('o',2):0.42,('o',3):0.32,  ('o',4):0.22, ('o',5):0.12,
        ('f',1):0.53, ('f',2):0.43,('f',3):0.33,  ('f',4):0.23, ('f',5):0.13,
        ('a',1):0.54, ('a',2):0.44,('a',3):0.34,  ('a',4):0.24, ('a',5):0.14,
        ('t',1):0.55, ('t',2):0.45,('t',3):0.35,  ('t',4):0.25, ('t',5):0.15,
        ('e',1):0.56, ('e',2):0.46,('e',3):0.36,  ('e',4):0.26, ('e',5):0.16,}


def word2kek(word):
    vowel_count = 0
    word_order = []
    unique = len(set(word))
    letter_freq = []
    usage = 0
    for i in range(len(word)):
        curr = word[i]
        if curr in vowels:
            vowel_count+=1
        letter_freq.append(freq[curr])
        word_order.append(order[(curr,i+1)])
    kek = [vowel_count,word_order,unique,letter_freq,usage]
    return kek



    