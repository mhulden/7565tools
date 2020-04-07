import sys

lang = sys.argv[1]

lines = [l.strip() for l in open(lang + '.trn')]

tags = sorted(list({l.split('\t')[2] for l in lines}))
lemmas = sorted(list({l.split('\t')[0] for l in lines}))

entries = {l:{} for l in lemmas}

for l in lines:
    lemma, form, tagstring = l.split('\t')
    entries[lemma][tagstring] = form
    
for lemma in lemmas:
    for tag in tags:
        if tag in entries[lemma]:
            print(lemma + '\t' + entries[lemma][tag] + '\t' + tag)
        else:
            print(lemma + '\t' + '-' + '\t' + tag)
