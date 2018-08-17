
import sys,codecs
import string

def init_lexicon(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lexicon = [x.rstrip('\r\n') for x in f]
 return lexicon

def get_alphabet(lexicon):
 alphabet = set()
 for word in lexicon:
  alphabet = alphabet.union(word)
 # sort letters
 letters = sorted(list(alphabet))
 return ''.join(letters)

if __name__ == "__main__":
 filein = sys.argv[1] # list of words (lexicon)
 fileout = sys.argv[2] # one line unicode string containing all letters used.

 lexicon = init_lexicon(filein)
 alphabet = get_alphabet(lexicon)
 print(len(alphabet),"letters used in words of",filein)
 with codecs.open(fileout,"w","utf-8") as f:
  f.write(alphabet + '\n')
 

