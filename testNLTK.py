import nltk
# nltk.download('punkt')
from nltk.corpus import stopwords

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

import numpy as np
from numpy.core.numeric import full





ignored_words = set(stopwords.words('french'))


filterStops = lambda w: len(w) < 3 or w in ignored_words

path_doc = "psgTest1_no_smiley.txt"

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



print(finder.nbest(BigramAssocMeasures.raw_freq, 30))



# bigram_measures = nltk.collocations.BigramAssocMeasures()
# print(finder.nbest(bigram_measures.pmi, 100))

# fdist = nltk.FreqDist(finder.nbest(bigram_measures.raw_freq, 100))
# for k,v in fdist.items():
#     print(k,v)

print(type(textword))
textword = [word for word in textword if word not in ignored_words]
fulltext = ""
for k in range (len(textword)) :
        fulltext += textword[k] + " "
fdist = FreqDist()

# for word in word_tokenize(fulltext) :
#         reader = f
#         freq_all = nltk.FreqDist()
#         fdist[word.lower()] += 1

# fdist.plot(20, cumulative = False)    

bgs = nltk.bigrams(textword)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
# for k,v in fdist.items():

fdist.plot(30)

# bigram_fd = nltk.FreqDist(nltk.bigrams(fulltext))

# print(bigram_fd.most_common())
# # Calculate raw frequency distribution
# freq = nltk.FreqDist(tokens) 
# freq_all.update(tokens)
# for key,val in freq.items(): 
#         print (str(key) + ':' + str(val))

# # Plot the results
# freq.plot(20, cumulative=False)

# # Plot the overall results
# freq_all.plot(20, cumulative=False)