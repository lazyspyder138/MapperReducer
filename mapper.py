#!/usr/bin/python3
import sys
import os
import re
import glob
import math
from collections import defaultdict
from functools import reduce
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import punkt
STOPWORDS = set(stopwords.words("english"))
def pre_processing(doc):
    terms = word_tokenize(doc)
    regex = re.compile(r"[^a-zA-Z0-9\s]")
    terms = [re.sub(regex, "", term) for term in terms]
    regex = re.compile(r"\d")
    terms = [re.sub(regex, "", term) for term in terms]
    # Remove stopwords and convert remaining terms to lowercase
    terms = [term.lower() for term in terms if term.lower() not in STOPWORDS]
    return terms
#Word Count Example
loc=0
# input comes from standard input STDIN
for line in sys.stdin:
            doc_id = os.environ["map_input_file"]
            doc_id = os.path.basename(doc_id)
            line = line.strip() #remove leading and trailing whitespaces
            terms = pre_processing(line)
            #words = line.split() #split the line into words and returns as a list
            for word in terms:
                #write the results to standard output STDOUT
                print('%s\t%s:%s' % (word,doc_id,loc)) 
                #Emit the word
                loc=loc+len(word)+1
