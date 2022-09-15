modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']
print(modern_family)
en1 = enumerate(modern_family)
indices = []
characters = []
for count,chars in en1:
    indices.append(count)
    characters.append(chars)

for i in range(len(characters)):
    characters[i] = characters[i].lower().replace('_','-')

temp = []
ans = map(lambda word: len(word),characters)
temp = list(ans)

zipped = zip(indices,temp)
indices = list(zipped)
for j in range(len(indices)):
    indices[j] = sum(indices[j])

indices.sort(reverse=True)

Phew_finally = {}
for i in range(len(indices)):
    Phew_finally[indices[i]] = characters[i]

print(Phew_finally)