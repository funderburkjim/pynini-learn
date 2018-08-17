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

class PWIS2(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split(' ')
  # two types:
  (self.iast,self.count,self.slp1) = parts[0:3]
  if len(parts) == 3:
   self.suggest = None
   self.suggestcode = None
  elif len(parts) == 5:
   (self.suggest,self.suggestcode) = parts[3:5]
  else:
   # unexpected
   print("ERROR: unexpected input from",filein)
   print(line)
   exit(1)

def init_pwis(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [PWIS2(x) for x in f]
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
 filein = sys.argv[3]  # pwis_notmw2.txt
 fileout = sys.argv[4] # 

 alphabet = init_alphabet(filealphabet)
 la = LevenshteinAutomaton(alphabet,lopath=filela)
 recs = init_pwis(filein)
 update_recs(recs,la)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   if rec.suggest != None:
    out = '%s %s %s %s %s' %(rec.iast,rec.count,rec.slp1,rec.suggest,rec.suggestcode) 
   else:
    out = '%s %s %s' %(rec.iast,rec.count,rec.slp1)      
   f.write(out + '\n')\

