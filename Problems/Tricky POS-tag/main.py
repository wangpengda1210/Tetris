import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

for word, pos in nltk.pos_tag(sent):
    if word == 'raced':
        print(pos)
