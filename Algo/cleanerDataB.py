import os
import re
from nltk import text
from deep_translator import GoogleTranslator

bad_words = ['created at :', 'followers count :', 'fav count :' ]

path_of_the_directory= 'RawData\\baltha\\vMathis'
for filename in os.listdir(path_of_the_directory):
    newFileName = "Mat"+filename
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        with open(f, encoding='utf8') as oldfile, open(newFileName, 'w', encoding="utf8") as newfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in bad_words):
                    newfile.write(line)