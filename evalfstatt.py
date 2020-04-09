import attapply
import sys, os

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

haslex = False
T = attapply.ATTFST(lang + '.att')
if os.path.isfile(lang + ".lex.att"):
    haslex = True
    TL = attapply.ATTFST(lang + ".lex.att")
    

evallines = [l.strip() for l in open(lang + evalextension)]

numguesses = 0
numcorrect = 0

for l in evallines:
    lemma, form, tags = l.split('\t')
    tstring = tagstobrackets(tags)
    haslexguess = False
    if haslex: # Apply lexicon-based guess with priority
        guesses = list(TL.apply(lemma + tstring))
        if len(guesses) > 0:
            haslexguess = True
            guess = guesses[0][0]
    if haslexguess == False:
        guesses = list(T.apply(lemma + tstring))
        if len(guesses) == 0:
            guess = 'NO OUTPUT'
        else:
            guess = guesses[0][0]
    if guess == form:
        numcorrect += 1
    else:
        print("ERROR:", lemma+tstring, guess, "SHOULD BE:", form)
    numguesses += 1
    
print("ACCURACY:", lang, numcorrect/numguesses)
