from foma import *
import sys, os

def tagstobrackets(s):
    tags = s.split(';')
    taglist = ["[" + t + "]" for t in tags]
    return ''.join(taglist)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
lang = sys.argv[1]

haslex = False
T = FST.load(lang + ".fomabin")
if os.path.isfile(lang + ".lex.fomabin"):
    haslex = True
    TL = FST.load(lang + ".lex.fomabin")

evallines = [l.strip() for l in open(lang + ".tst")]

outfile = open(lang + ".out", "w")

for l in evallines:
    lemma, tags = l.split('\t')
    tstring = tagstobrackets(tags)
    haslexguess = False
    if haslex: # Apply lexicon-based guess with priority
        guesses = list(TL.apply_down(lemma + tstring))
        if len(guesses) > 0:
            haslexguess = True
            guess = guesses[0]
    if haslexguess == False:
        guesses = list(T.apply_down(lemma + tstring))
        if len(guesses) == 0:
            guess = lemma # We're guessing the lemma if grammar doesn't know
            eprint("Warning:", lemma, tags, "has no output! Repeating lemma.")
        else:
            guess = guesses[0]
    outfile.write(lemma + "\t" + guess + "\t" + tags + "\n")
