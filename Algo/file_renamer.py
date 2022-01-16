import os 



path_of_the_directory= 'translated\\toChangeName'
for filename in os.listdir(path_of_the_directory):
    newFileName = filename[6:]
    os.rename(path_of_the_directory+ "\\"  +filename, newFileName)
