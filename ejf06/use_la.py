from tested import *

import sys,codecs
import string

def init_lexicon(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lexicon = [x.rstrip('\r\n') for x in f]
 return lexicon
def init_alphabet(filein):
 with codecs.open(filein,"r","utf-8") as f:
  x = f.readline()
 letterstring = x.rstrip('r\n')
 return letterstring

if __name__ == "__main__":
 filealphabet = sys.argv[1] # string of letters used in lexicon
 filein = sys.argv[2] # list of words (lexicon)
 #fileout = sys.argv[2] # compiled Levenshtein Automaton for the lexicon
 #lexicon = init_lexicon(filein)
 alphabet = init_alphabet(filealphabet)
 la = LevenshteinAutomaton(alphabet,lopath=filein)
 while True:
  x = raw_input('Enter word (q to quit):')
  if x == 'q':
   break
  #y = list(la.closest_matches(x))
  #y = list(la.closest_matches(x).encode('utf-8'))
  y = [z.encode('utf-8') for z in la.closest_matches(x)]
  print('closest:',y)


