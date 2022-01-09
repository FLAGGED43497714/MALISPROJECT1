from textblob import TextBlob


# with open("output_parallel.txt", 'r', encoding='utf-8') as file:
#     data = file.read()

# data = "J'aime la vie, je suis en pleine forme, je me sens très bien en ce moment"

b = TextBlob("J'aime la vie, je suis en pleine forme, je me sens très bien en ce moment").translate(from_lang="fr",to="en")


print(b.sentiment)




