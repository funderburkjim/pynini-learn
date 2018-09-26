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

class BUR(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split(' ')
  # two types:
  (self.buriast,self.count,self.iast,self.slp1) = parts[0:4]
  if len(parts) == 4:
   self.suggest = None
   self.suggestcode = None
  else:
   # unexpected
   print("ERROR: unexpected input from",filein)
   print(line)
   exit(1)

def init_bur(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [BUR(x) for x in f]
 #recs = recs[0:5]
 #print("init_bur restricts to first 5 records")
 return recs

def update_recs(recs,la):
 for irec,rec in enumerate(recs):
  if rec.suggest == None:
   #print(irec)
   try:
    matches = la.closest_matches(rec.slp1)
    y = list(matches) 
    rec.suggest = ','.join(y)
    rec.suggestcode = '(LevAuto)'
   except Exception as e:
    print("Error with",rec.slp1,e)

if __name__ == "__main__":
 filealphabet = sys.argv[1] # string of letters used in lexicon
 filela = sys.argv[2] # list of words (lexicon)
 filein = sys.argv[3]  # bur_input.txt
 fileout = sys.argv[4] # # bur_output.txt

 alphabet = init_alphabet(filealphabet)
 la = LevenshteinAutomaton(alphabet,lopath=filela)
 recs = init_bur(filein)
 update_recs(recs,la)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   if rec.suggest != None:
    out = '%s %s %s %s %s %s' %(rec.buriast,rec.count,rec.iast,rec.slp1,rec.suggest,rec.suggestcode) 
   else:
    out = '%s %s %s %s' %(rec.buriast,rec.count,rec.iast,rec.slp1)      
   f.write(out + '\n')\

