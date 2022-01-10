# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:14:50 2022

@author: mathi
"""

from textblob import TextBlob
from googletrans import Translator
from deep_translator import GoogleTranslator
import re
import numpy as np 
import pandas as pd

THE_data_csv = "fichier_test2.csv"

# THE_data_tab = np.genfromtxt(THE_data_csv,delimiter=",", dtype=str)

# THE_data_csv = "CleanData\\fichier_testMathis.csv"

THE_df = pd.read_csv(THE_data_csv)


#To complete



link_hometeam = "En-Venezia_Juv_Vene_11_12.txt"
link_awayteam= "En-Venezia_Juv_Juv_11_12.txt"

english = True




fileH=open(link_hometeam, encoding="utf8")
tmpH=fileH.read().split("\n\n\n\n")
tmpH.pop()
#print(tmp)

tableauH=[]
HomeAvgPolarity=0
HomeAvgSubj=0
#translator = Translator()

nb_zero_home = 0

for i in range(len(tmpH)):
    new_text = tmpH[i]
    new_text = re.sub(r'http\S+', '', new_text)
    new_text = re.sub(r'#\S+', '', new_text) #remove # and link
    
    #if (translator.detect(new_text).lang="en"):
     #   print("yo")
      #  translated=translator.translate(new_text)
      #  print(translated)
    #if blob.detect_language()!="en":
        #blob.translate(to="en") #translation into english
    
    if not english :
        new_text = GoogleTranslator(source='auto', target='en').translate(new_text)
    print(i,"->",len(tmpH))
    
    blob=TextBlob(new_text)
    sentiment=[blob.sentiment.polarity,blob.sentiment.subjectivity]
    tableauH.append(sentiment)
    HomeAvgPolarity+=sentiment[0]
    HomeAvgSubj+=sentiment[1]


    if sentiment[0] == 0 and sentiment[1] == 0 : 
        nb_zero_home+=1

    
print(tableauH)

print(nb_zero_home)

HomeAvgPolarity=HomeAvgPolarity/(len(tableauH) - nb_zero_home)
HomeAvgSubj= HomeAvgSubj/(len(tableauH) - nb_zero_home)



fileA=open(link_awayteam, encoding="utf8")
tmpA=fileA.read().split("\n\n\n\n")
tmpA.pop()
#print(tmp)

tableauA=[]
AwayAvgPolarity=0
AwayAvgSubj=0
#translator = Translator()
nb_zero_away = 0

for i in range(len(tmpA)):
    new_text = tmpA[i]
    new_text = re.sub(r'http\S+', '', new_text)
    new_text = re.sub(r'#\S+', '', new_text) #remove # and link
        
    if not english :
        new_text = GoogleTranslator(source='auto', target='en').translate(new_text)
    print(i,"->",len(tmpA))
    
    blob=TextBlob(new_text)
    sentiment=[blob.sentiment.polarity,blob.sentiment.subjectivity]
    tableauA.append(sentiment)
    AwayAvgPolarity+=sentiment[0]
    AwayAvgSubj+=sentiment[1]


    if sentiment[0] == 0 and sentiment[1] == 0 : 
        nb_zero_away+=1

    
    
print(tableauA)
print("nb_zero_away")
print(nb_zero_away)

AwayAvgPolarity=AwayAvgPolarity/(len(tableauA) - nb_zero_away )
AwayAvgSubj=AwayAvgSubj/(len(tableauA) - nb_zero_away )

# the_new_element = {
#     'HomeTeam' : link_hometeam.split('_')[0],
#     'AwayTeam' : link_hometeam.split('_')[1],
#     'HomeAvgPolarity' : HomeAvgPolarity,
#     'HomeAvgSubj' : HomeAvgSubj,
#     'AwayAvgPolarity' : AwayAvgPolarity,
#     'AwayAvgSubj' : AwayAvgSubj
# }

new_element = [link_hometeam.split('_')[0],link_hometeam.split('_')[1],HomeAvgPolarity,HomeAvgSubj,AwayAvgPolarity,AwayAvgSubj]

print(new_element)

THE_df.loc[len(THE_df)] = new_element
print(THE_df)

THE_df.to_csv("fichier_test2.csv",index=None)


