import nltk
from nltk.corpus import stopwords

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist

import numpy as np





ignored_words = set(stopwords.words('spanish'))


filterStops = lambda w: len(w) < 3 or w in ignored_words

path_doc = "Done\MatReading_Fulham_Reading11_01_2022.txt"



f = open(path_doc, "r", encoding='utf-8')

textword = np.array(f.read())


def readFile(fileName):
        fileObj = open(fileName, "r", encoding='utf8') #opens the file in read mode
        words = fileObj.read().split() #puts the file into an array
        fileObj.close()
        return words

textword = readFile(fileName=path_doc)

finder = BigramCollocationFinder.from_words(textword)

finder.apply_word_filter(filterStops)



# print(finder.nbest(BigramAssocMeasures.likelihood_ratio, 10))



print(finder.nbest(BigramAssocMeasures.raw_freq, 50))





print(type(textword))
textword = [word for word in textword if word not in ignored_words]
fulltext = ""
for k in range (len(textword)) :
        fulltext += textword[k] + " "
fdist = FreqDist()


bgs = nltk.bigrams(textword)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
# for k,v in fdist.items():

fdist.plot(30)
