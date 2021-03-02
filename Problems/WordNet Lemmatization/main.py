from nltk.stem import WordNetLemmatizer


# your code here
word_net = WordNetLemmatizer()
word = input()
print(word_net.lemmatize(word, pos='n'))
print(word_net.lemmatize(word, pos='a'))
print(word_net.lemmatize(word, pos='v'))
