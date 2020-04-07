import sys

lang = sys.argv[1]

linest = [l.strip() for l in open(lang + '.trn')]
linesd = [l.strip() for l in open(lang + '.dev')]

lemmast = {l.split('\t')[0] for l in linest}
lemmasd = {l.split('\t')[0] for l in linesd}

print(len(lemmast), " lemmas in train")
print(len(lemmasd), " lemmas in dev")
print(len(lemmast & lemmasd), " in common")
