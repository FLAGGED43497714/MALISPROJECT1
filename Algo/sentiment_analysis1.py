from textblob import TextBlob


with open("output_parallel.txt", 'r', encoding='utf-8') as file:
    data = file.read()



blob = TextBlob(data)


print(blob.sentiment)




