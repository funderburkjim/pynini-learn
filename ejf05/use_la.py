from tested import *

import sys,codecs
import string

def init_lexicon(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lexicon = [x.rstrip('\r\n') for x in f]
 return lexicon

if __name__ == "__main__":
 filein = sys.argv[1] # compiled Levenshtein Automaton 
 #fileout = sys.argv[2] # compiled Levenshtein Automaton for the lexicon
 #lexicon = init_lexicon(filein)
 la = LevenshteinAutomaton(string.ascii_letters,lopath=filein)
 for x in ["rockford","cheesesure"]:
  y = list(la.closest_matches(x))
  print(x,y)


