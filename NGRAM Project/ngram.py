#
#PA2
#Author: Christian Romero Taipe
#date: 5/9/2021
#Description:
#This program uses NLTK to create an ngram model based on a document and creates a random sentence.
#It uses user input to identify the documnet, the number of ngrms and the number of senteces to generate.
#

from sys import argv
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import re, random

# this function is used to create ngram
def extract_ngrams(data, num):
    n_grams = ngrams(data, num)
    return [' '.join(grams) for grams in n_grams]


# retrive to command the number of ngram, # of sentence and the name of books
ngram = int(argv[1])
n_sentence = int(argv[2])
books = argv[3:]

# initialization of array
text_ngram = []

for i in range(len(books)):
    file = open(books[i], encoding="utf8")
    lines = file.read().replace("\n", " ")
    # the regex is used to separate each sentence based on symbol .!?
    sentence = re.findall('[a-z0-9][^.!?]+\?|[a-z0-9][^!?.]+\!|[a-z0-9][^!.?]+\.', lines.lower())
    for k in range(len(sentence)):
        real_data = word_tokenize(sentence[k])
        if ngram <= len(real_data):
            #used + instead of append to have all the ngram in one list
            text_ngram = text_ngram + (extract_ngrams(real_data, ngram))
    file.close()

# count is used to count the number of sentence made
count = 0

while count != n_sentence:
    start_seq = random.choice(text_ngram)
    print(start_seq)
    if (re.findall('[a-z0-9][^.!?]+\?|[a-z0-9][^!?.]+\!|[a-z0-9][^!.?]+\.', start_seq)):
        print("\n")
        count = count + 1