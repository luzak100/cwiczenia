vowels=set('aeiou')
word=input("Podaj słowo, w którym należy wyszukać samogłoski: ")
i=vowels.intersection(set(word))

print(i)