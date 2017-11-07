from unicodedata import normalize

# with open('tokens_en.txt', 'w') as f:

#     for line in open('vader_lexicon_en.txt'):
#         token = line.split('\t')[0]    
        
#         f.write(token + '\n')

def normaliza_ptbr(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

tokens_en = [t.strip() for t in open('tokens_en.txt')]
tokens_pt = [normaliza_ptbr(t.strip()).lower() for t in open('tokens_pt.txt')]

print(tokens_en[:10])
print(tokens_pt[:10])

pares ={}
for i, t in enumerate(tokens_en):
    pares[t] = tokens_pt[i]

f = open('vader_lexicon.txt', 'w')

for line in open('vader_lexicon_en.txt'):
    line = line.split('\t')
    if line[0] in pares:
        line[0] = pares[line[0]]

    new_line = '\t'.join(line)

    f.write(new_line)

f.close()