import os

# string = "test string é â"

# path_out = "En_RawData\\mathis\\toTranslate\\Caen_Guingamp_Caen_11_12.txt"



# with open(path_out, "w", encoding="UTF-8") as f :
#     f.write(string)
#     f.close()


path_of_the_directory= 'RawData\mathis\\toTranslate'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        print(filename)
