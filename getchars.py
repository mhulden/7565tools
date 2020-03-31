import sys
lines = [l.strip() for l in open(sys.argv[1])]
alphabet = set()
for l in lines:
    lemma, form, _ = l.split('\t')
    alphabet |= set(lemma) | set(form)

print('[' + '|'.join(sorted(list(alphabet))) +']')
