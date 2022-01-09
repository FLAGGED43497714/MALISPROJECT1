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


#To complete
link_hometeam="Caen_Guingamp_Caen_11_12.txt"
link_awayteam="Caen_Guingamp_Guingamp_11_12.txt"





fileH=open("Data1/"+link_hometeam, encoding="utf8")
tmpH=fileH.read().split("\n\n\n\n")
tmpH.pop()
#print(tmp)

tableauH=[]
HomeAvgPolarity=0
HomeAvgSubj=0
#translator = Translator()

for i in range(len(tmpH)):
    new_text = tmpH[i]
    new_text = re.sub(r'http\S+', '', new_text)
    new_text = re.sub(r'#\S+', '', new_text) #remove # and link
    
    #if (translator.detect(new_text).lang!="en"):
     #   print("yo")
      #  translated=translator.translate(new_text)
      #  print(translated)
    #if blob.detect_language()!="en":
        #blob.translate(to="en") #translation into english
        
    new_text = GoogleTranslator(source='auto', target='en').translate(new_text)
    print(i,"->",len(tmpH))
    
    blob=TextBlob(new_text)
    sentiment=[blob.sentiment.polarity,blob.sentiment.subjectivity]
    tableauH.append(sentiment)
    HomeAvgPolarity+=sentiment[0]
    HomeAvgSubj+=sentiment[1]
    
print(tableauH)

HomeAvgPolarity=HomeAvgPolarity/len(tableauH)
HomeAvgSubj= HomeAvgSubj/len(tableauH)



fileA=open("Data1/"+link_awayteam, encoding="utf8")
tmpA=fileA.read().split("\n\n\n\n")
tmpA.pop()
#print(tmp)

tableauA=[]
AwayAvgPolarity=0
AwayAvgSubj=0
#translator = Translator()

for i in range(len(tmpA)):
    new_text = tmpA[i]
    new_text = re.sub(r'http\S+', '', new_text)
    new_text = re.sub(r'#\S+', '', new_text) #remove # and link
          
    new_text = GoogleTranslator(source='auto', target='en').translate(new_text)
    print(i,"->",len(tmpA))
    
    blob=TextBlob(new_text)
    sentiment=[blob.sentiment.polarity,blob.sentiment.subjectivity]
    tableauA.append(sentiment)
    AwayAvgPolarity+=sentiment[0]
    AwayAvgSubj+=sentiment[1]
    
    
print(tableauA)

AwayAvgPolarity=AwayAvgPolarity/len(tableauA)
AwayAvgSubj=AwayAvgSubj/len(tableauA)


final_tab=[['HomeTeam', 'AwayTeam', 'HomeAvgPolarity', 'HomeAvgSubj', 'AwayAvgPolarity', 'AwayAvgSubj'],[link_hometeam.split('_')[0],link_hometeam.split('_')[1],HomeAvgPolarity,HomeAvgSubj,AwayAvgPolarity,AwayAvgSubj]]
np.savetxt("fichier_test.csv", final_tab, delimiter =",",fmt ='% s')


