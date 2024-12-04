def my_long_word (n,phrase):

 return [word for word in phrase.split() if len(word) > n]

print(my_long_word(4, "demain je vais voir Aicha concernant les ennoncés faut quils nous mette"))