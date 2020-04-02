import attapply
import sys

def tagstobrackets(s):
    tags = s.split(';')
    taglist = ["[" + t + "]" for t in tags]
    return ''.join(taglist)

mode = sys.argv[1]
lang = sys.argv[2]
if mode == "-t":
    evalextension = ".trn"
else:
    evalextension = ".dev"

T = attapply.ATTFST(lang + '.att')

evallines = [l.strip() for l in open(lang + evalextension)]

numguesses = 0
numcorrect = 0

for l in evallines:
    lemma, form, tags = l.split('\t')
    tstring = tagstobrackets(tags)
    guesses = list(T.apply(lemma + tstring, dir = 'down'))
    if len(guesses) == 0:
        guess = 'NO OUTPUT'
    else:
        guess = guesses[0][0] # should exist
    if guess == form:
        numcorrect += 1
    else:
        print("ERROR:", lemma+tstring, guess, "SHOULD BE:", form)
    numguesses += 1
    
print("ACCURACY:", lang, numcorrect/numguesses)
