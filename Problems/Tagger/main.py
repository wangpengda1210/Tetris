import nltk


# the line below reads a sentence from the input and converts it into a list
sent = input().split()

# your code here
print(nltk.pos_tag(sent))
