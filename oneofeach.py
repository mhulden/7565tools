import sys

lang = sys.argv[1]

lines = [l.strip() for l in open(lang + '.trn')]

tagcombos = set()

for l in lines:
    lemma, form, tags = l.split('\t')
    if tags not in tagcombos:
        tagcombos |= {tags}
        print(l)
