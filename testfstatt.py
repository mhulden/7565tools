import attapply
import sys, os

def tagstobrackets(s):
    tags = s.split(';')
    taglist = ["[" + t + "]" for t in tags]
    return ''.join(taglist)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
lang = sys.argv[1]

haslex = False
T = attapply.ATTFST(lang + '.att')
if os.path.isfile(lang + ".lex.att"):
    haslex = True
    TL = attapply.ATTFST(lang + ".lex.att")
    
evallines = [l.strip() for l in open(lang + ".tst")]

outfile = open(lang + ".out", "w")

for l in evallines:
    lemma, tags = l.split('\t')
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
            guess = lemma
            eprint("Warning: ", lemma, tags, "has no output! Repeating lemma.")
        else:
            guess = guesses[0][0]
    outfile.write(lemma + "\t" + guess + "\t" + tags + "\n")


