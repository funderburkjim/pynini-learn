
import sys,codecs

class HW2(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.pc, self.hw,self.line12,self.L) = line.split(':')

def init_lexiconhw2(filein):
 d = {}
 with codecs.open(filein,"r","utf-8") as f:
  for x in f:
   rec = HW2(x)
   hw = rec.hw
   d[hw]=True
 lexicon = d.keys()
 return lexicon

if __name__ == "__main__":
 filein = sys.argv[1] # xhw2.txt
 fileout = sys.argv[2] # lexicon (as list of distinct words)
 lexicon = init_lexiconhw2(filein)
 with codecs.open(fileout,"w","utf-8") as f:
  for word in lexicon:
   f.write(word+'\n')
 print(len(lexicon),"words written to",fileout)


