import os
import re
from nltk import text
from deep_translator import GoogleTranslator


path_of_the_directory= 'toTranslate'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        file = open(f, encoding="utf8")
        tabTw=file.read().split("\n\n\n\n")
        tabTw.pop()


        enTabTw = []

        # tweets to tab
        # and parallele english tab
        for i in range(len(tabTw)):
            new_text = tabTw[i]
            new_text = re.sub(r'http\S+', '', new_text)
            new_text = re.sub(r'#\S+', '', new_text) #remove # and link

            try:
                new_text = GoogleTranslator(source='auto', target='en').translate(new_text)
            except ConnectionError:
                print("ConnectionError")
                pass
            
            clear = lambda: os.system('cls')
            clear()
            print(str(100 * (i / len(tabTw))) + "%")
            
            enTabTw.append(new_text)
            
        # Writing tab

        print("Writing ...") 

        new_name = "En-"+filename

        conc_txt = ""

        for k in range(len(enTabTw)) :
            en_txt = enTabTw[k]
            conc_txt += en_txt + "\n\n\n\n"

        with open(new_name, "w", encoding="UTF-8") as f :
            f.write(conc_txt)
            f.close()
