phrase='Podaj jajko!'
plist=list(phrase)
print(phrase)
print(plist)
location=[0,2,2,6,6,6]
for i in location:

    plist.pop(i)

new_phrase=''.join(plist)
print(plist)
print(new_phrase)
0,3,4,5,9,10,11